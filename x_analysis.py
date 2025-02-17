import tweepy
import pandas as pd
import time

# Twitter API v2 Credentials
# Retrieve Twitter API credentials securely from environment variables
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Check if bearer token is missing
if not bearer_token:
    raise ValueError("❌ Missing Twitter Bearer Token! Set TWITTER_BEARER_TOKEN in environment variables.")

# Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=bearer_token)

# Define search query
query = "AI Technology -is:retweet lang:en"

# Parameters
max_tweets = 25  # Adjust based on your needs
batch_size = 25   # Number of tweets per request
next_token = None
all_tweets = []

# Fetch tweets in batches with pagination
while len(all_tweets) < max_tweets:
    try:
        tweets = client.search_recent_tweets(
            query=query,
            max_results=batch_size,
            tweet_fields=["created_at", "public_metrics", "text", "author_id"],
            next_token=next_token
        )

        # If no new tweets are returned, stop fetching
        if not tweets.data:
            print("No more tweets found.")
            break

        # Append new tweets to dataset
        all_tweets.extend(tweets.data)

        # Get the next pagination token
        next_token = tweets.meta.get("next_token")

        # Stop if there's no next page
        if not next_token:
            break

        # Sleep to avoid hitting API rate limits
        time.sleep(10)

    except tweepy.TooManyRequests:
        print("Rate limit reached. Sleeping for 15 minutes...")
        time.sleep(900)  # Sleep for 15 minutes before retrying
    except Exception as e:
        print(f"Error: {e}")
        break

# Store data in DataFrame
data = [[tweet.created_at, tweet.author_id, tweet.text, tweet.public_metrics["like_count"], tweet.public_metrics["retweet_count"]] for tweet in all_tweets]
df = pd.DataFrame(data, columns=["Date", "User ID", "Tweet", "Likes", "Retweets"])

# Save data to CSV
df.to_csv("tweets.csv", index=False)

print(f"✅ Data collection completed! {len(df)} tweets saved.")
df.head()

import re

# Function to clean tweet text
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)  # Remove mentions (@username)
    text = re.sub(r"#\w+", "", text)  # Remove hashtags
    text = re.sub(r"[^A-Za-z\s]", "", text)  # Remove special characters
    return text.lower()

df["Cleaned_Tweet"] = df["Tweet"].apply(clean_text)

# Save cleaned data
df.to_csv("cleaned_tweets.csv", index=False)

print("✅ Data cleaning completed!")
df.head()

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon (one-time requirement)
nltk.download("vader_lexicon")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to determine sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Cleaned_Tweet"].apply(get_sentiment)

# Save sentiment data
df.to_csv("sentiment_analysis.csv", index=False)

print("✅ Sentiment analysis completed!")
df.head()

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 📊 Sentiment Distribution
plt.figure(figsize=(8,5))
sns.countplot(x=df["Sentiment"], palette="coolwarm")
plt.title("Sentiment Distribution of Tweets")
plt.show()

# 📈 Likes Over Time
df["Date"] = pd.to_datetime(df["Date"])
df.groupby(df["Date"].dt.date)["Likes"].sum().plot(kind="line", figsize=(10,5), marker="o")
plt.title("Total Likes Over Time")
plt.xlabel("Date")
plt.ylabel("Total Likes")
plt.show()

# ☁️ Word Cloud (Most Used Words)
text = " ".join(df["Cleaned_Tweet"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

