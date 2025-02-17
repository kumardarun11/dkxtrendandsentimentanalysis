# 📊 DK X Sentiment Analysis Dashboard

## 🚀 Overview

This project is a **Twitter (X) Sentiment Analysis Dashboard**, which collects, processes, and visualizes sentiment trends from tweets related to AI technology. The dashboard is built using **Python, Tweepy, Pandas, Streamlit, and Plotly**.

## 🔗 **Live Demo:** [DK YouTube Trending Analysis Dashboard](https://dkxtrendandsentimentanalysis-bexdblctqvnxmdymyntvb2.streamlit.app/)

## 📌 Features

- ✅ **Tweet Collection**: Fetches real-time tweets using Twitter API.
- ✅ **Data Cleaning**: Removes URLs, mentions, hashtags, and special characters.
- ✅ **Sentiment Analysis**: Classifies tweets as **Positive, Negative, or Neutral** using VADER sentiment analysis.
- ✅ **Data Visualization**: Provides interactive charts for sentiment trends, engagement, and word clouds.
- ✅ **Top Hashtags & Tweets**: Displays trending hashtags and most engaging tweets.
- ✅ **User-friendly Dashboard**: Built with **Streamlit** for easy data exploration.

## 📁 Project Structure

```
📂 DK_X_Sentiment_Analysis
│── 📜 x_analysis.py      # Collects and processes Twitter data
│── 📜 dashboard.py       # Streamlit dashboard for visualization
│── 📜 sentiment_analysis.csv  # Processed tweet data with sentiment scores
│── 📜 cleaned_tweets.csv      # Preprocessed tweet text
│── 📜 tweets.csv              # Raw tweet dataset
│── 📜 requirements.txt   # Required dependencies
│── 📜 README.md          # Project documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/DK_X_Sentiment_Analysis.git
   cd DK_X_Sentiment_Analysis
   ```
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Twitter API credentials**

   - Create a `config.py` file and add your **Twitter API credentials**:
     ```python
     BEARER_TOKEN = "your_bearer_token_here"
     ```
4. **Run the tweet collection script**

   ```bash
   python x_analysis.py
   ```
5. **Launch the Streamlit dashboard**

   ```bash
   streamlit run dashboard.py
   ```

## 🖥️ Dashboard Preview

The dashboard provides **interactive visualizations** for tweet sentiment analysis, including:

- 📊 **Sentiment Distribution**
- ☁️ **Word Cloud of Most Used Words**
- 📈 **Likes Over Time**
- 🔥 **Top 5 Most Liked Tweets**
- 🏷️ **Trending Hashtags**

## 📷 Screenshots

### 1️⃣Sentiment Distribution

!(https://github.com/user-attachments/assets/19d6cf5f-84d4-4e07-ad9f-04861b01a095)

### 2️⃣Most Used Words in Tweets

!(https://github.com/user-attachments/assets/018ded66-29a6-4275-b228-c4b61437d443)

### 3️⃣Likes Over Time & Most Liked Tweets

!(https://github.com/user-attachments/assets/75fc4d6e-f193-4644-8c53-00d9472da951)

### 4️⃣Trending Hashtags

!(https://github.com/user-attachments/assets/68ced3d8-b452-43da-8530-0eb8c8f98fc6)

## 📜 License

This project is licensed under the **MIT License**.

## 🎖️ Author

Developed by **D ARUN KUMAR**
🚀 **Powered by Streamlit & Plotly**

---

Enjoy analyzing X sentiment trends! If you like this project, ⭐ star the repository!
