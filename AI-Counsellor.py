import streamlit as st
import google.generativeai as genai

api_key = st.secrets["api_key"]
# Configure the generative AI model and API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Student Career Counselor Chatbot")

# Initial chatbot response
response = model.generate_content("Act as a Student Career Counselor. Hello!")
st.write("Hello, I'm your Student Career Counselor, how can I help you?")

user_message = st.text_area("Enter your message:")
submit_button = st.button("Submit")

if submit_button:
    if user_message:
        prompt = f"You: {user_message}\nCounselor:"
        response = model.generate_content(prompt)
        st.write("Bot:", response.text)
        user_message = ""  # Clear the text area after submission
