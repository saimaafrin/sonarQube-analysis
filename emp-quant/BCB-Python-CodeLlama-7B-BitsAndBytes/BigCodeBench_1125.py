
import re
import json
import requests

def task_func(myString, token):
    # Extract the first URL from the string
    url = re.search(r'https?://\S+', myString).group()

    # Create a JSON payload with the URL
    payload = {'url': url}

    # Set the headers with the authorization token
    headers = {'Authorization': f'Bearer {token}'}

    # Make the POST request to the API
    response = requests.post(url, json=payload, headers=headers)

    # Return the response from the API
    return response.json()