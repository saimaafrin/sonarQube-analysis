
import re
import json
import requests

def task_func(myString, token):
    # Extract the URL from the string
    url_match = re.search(r'https?://\S+', myString)
    if url_match:
        url = url_match.group(0)
    else:
        raise ValueError('No URL found in string')

    # Create the JSON payload
    payload = {
        'url': url,
        'token': token
    }

    # Send the request to the API
    response = requests.post(url, json=payload)

    # Return the response
    return response.json()