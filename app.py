import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def load_model():
    """Loads the trained TF-IDF vectorizer and sentiment models."""
    with open('vectorizer.pkl', 'rb') as v_file:
        vectorizer = pickle.load(v_file)
    models = {}
    for model_name in ['Logistic Regression_model.pkl', 'Random Forest_model.pkl', 'Naïve Bayes_model.pkl']:
        with open(model_name, 'rb') as m_file:
            models[model_name.split('_model.pkl')[0].replace('_', ' ').title()] = pickle.load(m_file)
    return vectorizer, models

def predict_sentiment(text, vectorizer, model):
    """Predicts sentiment for a given text using the specified model."""
    text_transformed = vectorizer.transform([text])
    prediction = model.predict(text_transformed)
    return prediction[0]

# Streamlit UI
st.title("Twitter Sentiment Analysis")
st.write("Enter a tweet below to analyze its sentiment using different models.")

vectorizer, models = load_model()
selected_model = st.selectbox("Choose a Model", list(models.keys()))
user_input = st.text_area("Enter your tweet:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        sentiment = predict_sentiment(user_input, vectorizer, models[selected_model])
        st.write(f"**Predicted Sentiment:** {sentiment}")
    else:
        st.write("Please enter a valid tweet.")