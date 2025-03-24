# Twitter Sentiment Analysis

## 📌 Project Overview
This project performs **Sentiment Analysis on Twitter Data** using various **Machine Learning models**. It leverages **NLP techniques** to preprocess text data, extract features, and classify sentiments into categories. The project is optimized for large datasets using **Dask** and deployed using **Streamlit**.

## 🚀 Features
- **Handles Large Datasets Efficiently** using chunking and Dask
- **Text Preprocessing** including stopword removal, tokenization, and cleaning
- **Multiple ML Models** trained: Naïve Bayes, Logistic Regression, and Random Forest
- **Data Visualizations** using Seaborn and Plotly
- **Interactive Sentiment Analysis** via a Streamlit Web App

## 📂 Dataset
The dataset contains:
- **ID**: Tweet ID
- **Category**: Type of tweet
- **Sentiment**: Sentiment classification (Positive, Negative, Neutral)
- **Tweet**: Raw tweet text

## 🛠 Installation & Setup

Clone the repository:
```bash
git clone https://github.com/banner-subha/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🔄 Preprocess and Train Models
Run the script to preprocess data and train models:
```bash
python train_models.py
```
This will:
- Load and preprocess data
- Train ML models
- Save models and vectorizer as `.pkl` files

## 🎨 Visualizations
The project includes:
- **Sentiment Distribution Plots**
- **Confusion Matrices**
- **Word Clouds with Various Colormaps**
- **Model Performance Comparison**

## 🌐 Deploy Streamlit App
Run the Streamlit app to analyze tweets in real-time:
```bash
streamlit run app.py
```

## 📊 Results & Model Performance
| Model                 | Accuracy |
|----------------------|----------|
| Naïve Bayes          | 79%      |
| Logistic Regression  | 88%      |
| Random Forest       | 90%      |

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Feel free to **fork** this repo and contribute!

## ✨ Author
**Subhadeep Banerjee**

---
⭐ Don't forget to **star** this repo if you like it!
