
import re
import json
import requests

def task_func(myString, token):
    # Extract URLs using regular expression
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    if not urls:
        return "No URL found in the input string"
    
    # Use the first URL found
    url_to_send = urls[0]
    
    # Define the API endpoint
    api_url = 'https://example.com/api/endpoint'  # Replace with actual API endpoint
    
    # Create the JSON payload
    payload = {
        'url': url_to_send
    }
    
    # Set the headers including the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    # Send the POST request
    try:
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return str(e)