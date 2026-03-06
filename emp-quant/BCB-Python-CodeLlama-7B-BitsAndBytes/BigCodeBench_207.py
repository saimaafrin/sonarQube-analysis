
import re
import requests

def task_func(input):
    # Extract the API endpoint from the input string
    endpoint_match = re.search(r'https?://\S+', input)
    if endpoint_match:
        endpoint = endpoint_match.group()
    else:
        raise ValueError('No API endpoint found in input')

    # Send a GET request to the endpoint
    response = requests.get(endpoint)

    # Return the response data in JSON format
    return response.json()