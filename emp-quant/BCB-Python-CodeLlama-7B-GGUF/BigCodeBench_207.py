
import re
import requests

def task_func(input):
    # Extract the API endpoint from the input string
    endpoint = re.search(r'https?://\S+', input).group()

    # Send a GET request to the endpoint
    response = requests.get(endpoint)

    # Return the response data in JSON format
    return response.json()