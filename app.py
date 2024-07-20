import streamlit as st
import requests
import json
import os

st.title("Meta-Llama-3-70B-Instruct Q&A Chatbot")

# Fetching the endpoint URL and API key from environment variables
endpoint_url = os.getenv("ENDPOINT_URL")
api_key = os.getenv("API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Function to get the bot response
def get_response():
    user_input = st.session_state.user_input
    payload = json.dumps({"messages": [{"role": "user", "content": user_input}]})
    response = requests.post(endpoint_url, headers=headers, data=payload)

    if response.status_code == 200:
        result = response.json()
        st.session_state.bot_response = result['choices'][0]['message']['content']
    else:
        st.session_state.bot_response = f"Error: Unable to get response from the endpoint. Status Code: {response.status_code}. Response Text: {response.text}"

# Initialize session state
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

if 'bot_response' not in st.session_state:
    st.session_state.bot_response = ""

# Input text box for user queries
st.text_input("You: ", key='user_input', on_change=get_response)
st.text_area("Bot:", value=st.session_state.bot_response, height=200)

st.write("Ask any question and the chatbot will respond!")
