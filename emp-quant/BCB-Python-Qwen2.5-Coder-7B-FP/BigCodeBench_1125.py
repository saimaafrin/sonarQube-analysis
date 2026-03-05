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
        return "No URL found in the string"

    # Prepare the JSON payload
    payload = json.dumps({"url": url})

    # Set the headers with the authorization token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    # Send the POST request to the REST API
    response = requests.post("https://api.example.com/endpoint", data=payload, headers=headers)

    # Return the response from the API
    return response.json()