import streamlit as st
import requests
import json

st.title("Meta-Llama-3-70B-Instruct Q&A Chatbot")

# Endpoint URL and API key
endpoint_url = "https://Meta-Llama-3-70B-Instruct-adrnq.eastus2.models.ai.azure.com/v1/chat/completions"
api_key = "UWmruYOh5qVgR1sCYGqXm1uplBiEAFeV"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Function to send the request and display the response
def get_response():
    user_input = st.session_state.user_input
    if user_input:
        try:
            payload = json.dumps({
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            })
            
            response = requests.post(endpoint_url, headers=headers, data=payload)
            
            if response.status_code == 200:
                result = response.json()
                st.session_state.bot_response = result['choices'][0]['message']['content']
            else:
                st.session_state.bot_response = f"Error: Unable to get response from the endpoint. Status Code: {response.status_code}\nResponse Text: {response.text}"
        except Exception as e:
            st.session_state.bot_response = f"Exception: {str(e)}"
    else:
        st.session_state.bot_response = ""

# Input text box for user queries
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

if 'bot_response' not in st.session_state:
    st.session_state.bot_response = ""

st.text_input("You: ", key='user_input', on_change=get_response)

st.text_area("Bot:", value=st.session_state.bot_response, height=200)

st.write("Ask any question and the chatbot will respond!")
