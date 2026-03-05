import re
import urllib.request
import json
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
def task_func(API_URL):
    try:
        # Send a request to the API
        with urllib.request.urlopen(API_URL) as response:
            data = response.read()
            # Parse the JSON response
            json_data = json.loads(data)
            # Extract the public IP address using regex
            ip_address = re.search(IP_REGEX, json_data['ip']).group()
            return ip_address
    except Exception as e:
        # Return the error message if the API request fails
        return str(e)