import re
import json
import requests
def task_func(myString, token):
    """
    Extracts a URL from a string and sends it to a REST API via a POST request.
    The URL is included in the JSON payload, and an authorization token is used in the headers for API access.
    If multiple URLs are in myString, then use the first one.
    """
    # Extract the first URL from myString
    url = re.search(r'https?://\S+', myString).group()

    # Create a JSON payload with the URL
    payload = {'url': url}

    # Set the headers for the API request
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # Make the POST request to the API
    response = requests.post(url, headers=headers, json=payload)

    # Return the response from the API
    return response.json()
myString = 'This is a string with a URL: https://www.example.com/path/to/resource'
token = 'my_token'