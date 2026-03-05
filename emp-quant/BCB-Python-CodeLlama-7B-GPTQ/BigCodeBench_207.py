import re
import requests
def task_func(input):
    # Extract the API endpoint from the input string
    endpoint = re.search(r'https://api.example.com/v1/(.+?)(?=\?|$)', input).group(1)

    # Send a GET request to the endpoint
    response = requests.get(f'https://api.example.com/v1/{endpoint}')

    # Return the response data in JSON format
    return response.json()
input = 'https://api.example.com/v1/users?page=1'