
import re
import json
# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(ip_address):
    # Validate the IP address using the regex
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'
    
    # Create a JSON response with the IP address
    json_response = json.dumps({'ip': ip_address})
    
    # Parse the JSON response to get the IP address
    parsed_response = json.loads(json_response)
    
    # Return the public IP address
    return parsed_response['ip']