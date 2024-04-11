import streamlit as st
import google.generativeai as genai

# Configure Google Gemini
genai.configure(api_key="AIzaSyCr_kK6_ImVl25Q3dQmlYiwIdWRF3yhmhc")

# Initialize the chat model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Streamlit UI
st.title("Interactive Gen AI Bot")

# User input
user_input = st.text_input("You:")

# Send message to the chat model and display the response
if user_input:
    response = chat.send_message(user_input)
    st.write("Gemini: " + response.text)
