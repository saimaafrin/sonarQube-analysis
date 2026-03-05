
import re
import json
import requests

def task_func(myString, token):
    # Extract the first URL from the string using regular expression
    url_match = re.search(r'https?://[^\s]+', myString)
    if url_match:
        url = url_match.group(0)
    else:
        return "No URL found in the string"

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