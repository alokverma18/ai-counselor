import streamlit as st
import google.generativeai as palm

# Configure the generative AI model and API key
palm.configure(api_key='AIzaSyBZZBj_c1TDDWAYgDg8GUqGiJYX4uzSjxY')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

st.title("Student Career Counselor Chatbot")

# Initial chatbot response
response = palm.chat(context="Act like a Student Career Counsellor.", messages='Hello')
st.write("Hello, I'm your Student Career Counselor, how can I help you?")

user_message = st.text_input("Enter your message:")

if user_message:
    response = response.reply(user_message)
    st.write("Bot:", response.last)
