# Student Career Counselor Chatbot

This project is a Streamlit-based application that utilizes a generative AI model to simulate a Student Career Counselor chatbot. Users can interact with the chatbot by entering messages, and the bot responds accordingly.

## Setup

1. *Install Dependencies:*
   ```bash
   pip install streamlit
   pip install google.generativeai  
   ```

2. *Configure API Key:*
   Obtain an API key from the Google Generative AI service and set it in the code:
   python
   palm.configure(api_key='YOUR_API_KEY')
   

3. *Run the Application:*
   ```bash
   streamlit run AI-Cousellor.py
   ```

  

## Usage

1. Open the application in a web browser.

2. Enter your message in the input box.

3. The chatbot will respond with a simulated Student Career Counselor response.

## Project Structure

- AI-Councellor.py: The main script containing the Streamlit application code.
- requirements.txt: A file listing the project dependencies.

## Notes

- This project uses the Streamlit library for creating the web interface.
- The generative AI model from the Google Generative AI service is employed for chatbot responses.

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI Documentation](https://generativeai.dev/docs/)
