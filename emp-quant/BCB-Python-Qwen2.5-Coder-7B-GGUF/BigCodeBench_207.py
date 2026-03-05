
import re
import requests

def task_func(input):
    # Extract the API endpoint using regular expression
    api_endpoint = re.search(r'https?://[^\s]+', input)
    if api_endpoint:
        api_endpoint = api_endpoint.group(0)
        try:
            # Send a GET request to the API endpoint
            response = requests.get(api_endpoint)
            response.raise_for_status()  # Raise an exception for HTTP errors
            # Return the response data in JSON format
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {api_endpoint}: {e}")
            return None
    else:
        print("No API endpoint found in the input string.")
        return None