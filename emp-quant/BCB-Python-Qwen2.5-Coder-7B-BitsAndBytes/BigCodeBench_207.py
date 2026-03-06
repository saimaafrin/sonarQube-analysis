
import re
import requests

def task_func(input_str):
    # Extract the API endpoint using regular expression
    api_endpoint = re.search(r'https?://[^\s"]+', input_str)
    
    if api_endpoint:
        endpoint = api_endpoint.group(0)
        try:
            # Send a GET request to the extracted endpoint
            response = requests.get(endpoint)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Return the response data in JSON format
                return response.json()
            else:
                raise Exception(f"Failed to retrieve data: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the request: {e}")
    else:
        raise ValueError("No valid API endpoint found in the input string")