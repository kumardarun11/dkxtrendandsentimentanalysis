# 📊 DK X Sentiment Analysis Dashboard

## 🚀 Overview

This project is a **Twitter (X) Sentiment Analysis Dashboard**, which collects, processes, and visualizes sentiment trends from tweets related to AI technology. The dashboard is built using **Python, Tweepy, Pandas, Streamlit, and Plotly**.

## 🔗 **Live Demo:** [DK YouTube Trending Analysis Dashboard](https://dkxtrendandsentimentanalysis.streamlit.app/)

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

![image](https://github.com/user-attachments/assets/f763e27a-451f-45e7-a834-1e36e2ee9a7a)

### 2️⃣Most Used Words in Tweets

![image](https://github.com/user-attachments/assets/152792f9-0547-47a6-b26d-6a25e639515d)

### 3️⃣Likes Over Time & Most Liked Tweets

![image](https://github.com/user-attachments/assets/e240da14-f05a-4bbe-8d73-c82e891163fe)

### 4️⃣Trending Hashtags

![image](https://github.com/user-attachments/assets/2189ee52-5e5b-4289-bd4d-10a8eee07963)

## 📜 License

This project is licensed under the **MIT License**.

## 👨‍💻 **Developer**

**D ARUN KUMAR**
📧 kumardarun11@gmail.com
🔗 [GitHub](https://github.com/kumardarun11) | [LinkedIn](https://linkedin.com/in/kumardarun11)

---

Enjoy analyzing X sentiment trends! If you like this project, ⭐ star the repository!
