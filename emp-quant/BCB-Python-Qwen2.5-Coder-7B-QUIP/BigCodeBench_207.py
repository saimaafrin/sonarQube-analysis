
import re
import requests

def task_func(input):
    # Extract the API endpoint using regular expression
    match = re.search(r'https?://[^\s]*', input)
    if match:
        api_endpoint = match.group(0)
        # Send a GET request to the API endpoint
        response = requests.get(api_endpoint)
        # Return the response data in JSON format
        return dict(response.json())
    else:
        return {}