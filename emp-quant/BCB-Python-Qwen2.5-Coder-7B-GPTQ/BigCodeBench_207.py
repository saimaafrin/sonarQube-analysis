import re
import requests
def task_func(input):
    # Extract the API endpoint using regular expression
    match = re.search(r'https?://[^\s]+', input)
    if match:
        api_endpoint = match.group(0)
        # Send a GET request to the API endpoint
        response = requests.get(api_endpoint)
        # Check if the request was successful
        if response.status_code == 200:
            # Return the response data in JSON format
            return response.json()
        else:
            # Return an error message if the request failed
            return {'error': 'Failed to retrieve data'}
    else:
        # Return an error message if no API endpoint was found
        return {'error': 'No API endpoint found'}