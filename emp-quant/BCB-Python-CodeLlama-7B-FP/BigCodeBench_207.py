import re
import requests
def task_func(input):
    """
    Extract an API endpoint from the input string, send a GET request to the endpoint, and return the response data in JSON format.
    """
    # Extract the API endpoint from the input string
    endpoint = re.search(r'https://api.example.com/v1/([^/]+)', input).group(1)

    # Send a GET request to the endpoint
    response = requests.get(f'https://api.example.com/v1/{endpoint}')

    # Return the response data in JSON format
    return response.json()
input = 'https://api.example.com/v1/users'