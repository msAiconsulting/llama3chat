import requests
import json

# Updated endpoint URL and API key
endpoint_url = "https://Meta-Llama-3-70B-Instruct-adrnq.eastus2.models.ai.azure.com/v1/chat/completions"
api_key = "UWmruYOh5qVgR1sCYGqXm1uplBiEAFeV"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# User input
user_input = input("You: ")

# Adjusted payload to match typical chat completion API structure
payload = json.dumps({
    "messages": [
        {"role": "user", "content": user_input}
    ]
})

try:
    # Send request to the endpoint
    response = requests.post(endpoint_url, headers=headers, data=payload)
    
    # Print debugging information
    print(f"Endpoint URL: {endpoint_url}")
    print(f"Payload: {payload}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    # Display the response from the model
    if response.status_code == 200:
        result = response.json()
        print(f"Bot: {result['choices'][0]['message']['content']}")
    else:
        print(f"Error: Unable to get response from the endpoint. Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")
