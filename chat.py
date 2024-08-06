import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
from langdetect import detect, LangDetectException

# Initialize the SentimentIntensityAnalyzer and Translator
sent = SentimentIntensityAnalyzer()
translator = Translator()

# Streamlit app configuration
st.image("innomatics logo.jpg", width=350)
st.title("Multilingual Customer  Review Analysis")
st.image("shutterstock_409373569.jpg", width=450)

# Input text for review
text = st.text_input("Enter the review:")

# Function to detect and translate text
def detect_translate(text):
    try:
        language = detect(text)
        st.write(f"The text entered is in: {language}")
        translation = translator.translate(text,src=language, dest="en")
        translated_text = translation.text
        st.write(f"Original text: {text}")
        st.write(f"Translated text: {translated_text}")
        return translated_text
    except LangDetectException as e:
        st.write(f"Error detecting language: {e}")

    return None

#st.write(" * All languages are accepted")
# Handle the submit button
if st.button("Submit"):
    
    translated_text = detect_translate(text)
    
    if translated_text:
        score = sent.polarity_scores(translated_text)["compound"]

        if score >= 0.1:
            st.write("Positive Review")
            st.image("customer_feedback_positive.jpg")
        elif score <= -0.1:
            st.write("Negative Review")
            st.image("handle-negative-customer-reviews-01.webp")
        else:
            st.write("Neutral Review")
            st.image("agverage-netral1-emoticon-customer-service-260nw-1926542183.jpg")
