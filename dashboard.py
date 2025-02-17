import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud

# 📌 Load X data
df = pd.read_csv("sentiment_analysis.csv")

# 📌 Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# 🌟 Streamlit UI Enhancements
st.set_page_config(page_title="X Sentiment Dashboard", layout="wide")

st.title("📊 DK X Sentiment Analysis Dashboard")
st.markdown("### Analyze X data trends, sentiment, and engagement 📈")

# 🎨 Sidebar Filters
st.sidebar.header("🔍 Filter Tweets")
sentiment_filter = st.sidebar.multiselect("Select Sentiment", options=df["Sentiment"].unique(), default=df["Sentiment"].unique())
date_range = st.sidebar.date_input("Select Date Range", [df["Date"].min(), df["Date"].max()])

# Apply Filters
df_filtered = df[(df["Sentiment"].isin(sentiment_filter)) & (df["Date"].between(pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])))]

# 📊 Sentiment Distribution - Interactive Plot
st.subheader("📊 Sentiment Distribution")
fig = px.histogram(df_filtered, x="Sentiment", color="Sentiment", barmode="group", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# ☁️ Word Cloud
st.subheader("☁️ Most Used Words in Tweets")
text = " ".join(df_filtered["Cleaned_Tweet"])
wordcloud = WordCloud(width=1000, height=500, background_color="black", colormap="cool").generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# 📅 Likes Over Time - Interactive Line Chart
st.subheader("📈 Likes Over Time")
fig = px.line(df_filtered.groupby(df_filtered["Date"].dt.date)["Likes"].sum().reset_index(),
              x="Date", y="Likes", markers=True, template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# 🔥 Top 5 Most Engaging Tweets
st.subheader("🔥 Top 5 Most Liked Tweets")
st.dataframe(df_filtered.nlargest(5, "Likes")[["Date", "Tweet", "Likes"]])

# 🏷️ Trending Hashtags
st.subheader("🏷️ Trending Hashtags")
hashtags = df_filtered["Tweet"].str.findall(r"#\w+").explode()
top_hashtags = hashtags.value_counts().head(10)
fig = px.bar(x=top_hashtags.index, y=top_hashtags.values, labels={"x": "Hashtags", "y": "Count"}, template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# ℹ Developer Info
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 Developer Info")
st.sidebar.write("**Name:** D ARUN KUMAR")
st.sidebar.write("📧 Email: kumardarun11@gmail.com")
st.sidebar.write("[GitHub](https://github.com/kumardarun11) | [LinkedIn](https://linkedin.com/in/kumardarun11)")
