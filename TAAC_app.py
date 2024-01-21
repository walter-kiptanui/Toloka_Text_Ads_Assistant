# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:51:07 2024

@author: kiptanui
"""

# app.py
import streamlit as st
import pickle

#text
import nltk                   
nltk.download("stopwords")    
import string                
import re                     
import json                   
from bs4 import BeautifulSoup

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the pre-trained model
with open("mnb_classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load the CountVectorizer
with open("count_vectorizer.pkl", "rb") as vectorizer_file:
    count_vect = pickle.load(vectorizer_file)

space_replace = re.compile('[/(){}\[\]\|@,;)]')   
bad_symbols = re.compile('[^0-9a-z #+_]')         
stopwords = nltk.corpus.stopwords.words('english') 
urls = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|''[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' 'rt')

def text_cleaning(text):
    text = BeautifulSoup(text, "lxml").text 
    text = text.lower()                     
    text = space_replace.sub(' ', text)     
    text = bad_symbols.sub('',text)         
    text = ' '.join(word for word in text.split() if word not in stopwords)    
    text = urls.sub('', text)               
    return text

# Function to make predictions
def predict_relevance(text):
    cleaned_text = text_cleaning(text)
    text_features = count_vect.transform([cleaned_text])
    prediction = model.predict(text_features)
    
    return prediction

# Streamlit app
def main():
    st.title("Relevance Prediction App")

    # Input text area for user to enter text
    user_input = st.text_area("Enter text for relevance prediction:")

    # Button to trigger prediction
    if st.button("Predict"):
        if user_input:
            # Make prediction
            prediction = predict_relevance(user_input)
            st.success(f"Prediction: {prediction}")
            if prediction[0] > 0.5:
                st.success('Good Match')
            else:
                st.error('Predicted as Bad Match')
        else:
            st.warning("Please enter text for prediction.")

if __name__ == "__main__":
    main()
