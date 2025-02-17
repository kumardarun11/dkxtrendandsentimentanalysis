import pandas as pd
import random
import re
from datetime import datetime, timedelta
from faker import Faker
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize Faker and Sentiment Analyzer
fake = Faker()
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Function to generate fake tweets
def generate_fake_tweets(n=100):
    tweets = []
    start_date = datetime.now() - timedelta(days=7)  # Tweets from the last week

    for _ in range(n):
        created_at = start_date + timedelta(minutes=random.randint(0, 10080))  # Random time in the past week
        author_id = fake.random_int(min=1000, max=9999)
        text = fake.sentence(nb_words=random.randint(5, 15)) + " #Politics #Modi #BJP"
        likes = random.randint(0, 500)
        retweets = random.randint(0, 100)
        tweets.append([created_at, author_id, text, likes, retweets])
    
    return tweets

# Generate Fake Tweets
tweet_data = generate_fake_tweets(180)

# Save to tweets.csv
df = pd.DataFrame(tweet_data, columns=["Date", "User ID", "Tweet", "Likes", "Retweets"])
df.to_csv("tweets.csv", index=False)
print("✅ tweets.csv created!")

# Function to clean tweet text
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)  # Remove mentions
    text = re.sub(r"#\w+", "", text)  # Remove hashtags
    text = re.sub(r"[^A-Za-z\s]", "", text)  # Remove special characters
    return text.lower()

# Apply cleaning function
df["Cleaned_Tweet"] = df["Tweet"].apply(clean_text)

# Save cleaned tweets
df.to_csv("cleaned_tweets.csv", index=False)
print("✅ cleaned_tweets.csv created!")

# Function to determine sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Cleaned_Tweet"].apply(get_sentiment)

# Save sentiment analysis
df.to_csv("sentiment_analysis.csv", index=False)
print("✅ sentiment_analysis.csv created!")

# Display first few rows
df.head()

