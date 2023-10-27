# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:39:50 2023

@author: kiptanui
"""


import streamlit as st
import pickle
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

# Load your saved model
model_filepath = 'trained_model.h5'

loaded_model = load_model(model_filepath)

# Define the vocabulary size and sentence length (must match the preprocessing used during training)
voc_size = 10
sent_length = 10

# Function to make predictions
def predict_rel(predict_relevance):
    concatenated_text = ' '.join(predict_relevance)
    onehot_reprr = [one_hot(concatenated_text.lower(), voc_size)]
    padded = pad_sequences(onehot_reprr, maxlen=sent_length, padding='pre')
    return loaded_model.predict(padded)

# Streamlit UI
st.title("TAAC Text Classification Web App")

# Input text box for user input
user_input = st.text_input("Enter text for classification:")

if user_input:
    # Make predictions when the user provides input
    predictions = predict_rel([user_input])

    # Display the prediction results
    if predictions[0] > 0.5:
        st.success(f"Predicted as Good Match (Score: {predictions[0][0]})")
    else:
        st.error(f"Predicted as Bad Match (Score: {predictions[0][0]})")

