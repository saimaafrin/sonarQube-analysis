
import re
import requests

def task_func(input):
    # Extract the API endpoint from the input string
    pattern = r"https?://([a-zA-Z0-9-]+).?([a-zA-Z0-9-]+).?([a-zA-Z0-9-]+)/([a-zA-Z0-9-]+)"
    match = re.search(pattern, input)
    if match:
        endpoint = match.group(0)
    else:
        raise ValueError("Invalid input")

    # Send a GET request to the endpoint
    response = requests.get(endpoint)

    # Return the response data in JSON format
    return response.json()