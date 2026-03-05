import re
import json
import requests
def task_func(myString, token):
    # Extract the first URL from the string using regex
    url_pattern = re.compile(r'https?://[^\s]+')
    match = url_pattern.search(myString)
    if match:
        url = match.group(0)
    else:
        raise ValueError("No URL found in the input string")

    # Prepare the JSON payload with the extracted URL
    payload = {
        "url": url
    }

    # Set the headers with the authorization token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Send a POST request to the REST API
    response = requests.post("https://api.example.com/endpoint", headers=headers, data=json.dumps(payload))

    # Return the response from the API
    return response.json()