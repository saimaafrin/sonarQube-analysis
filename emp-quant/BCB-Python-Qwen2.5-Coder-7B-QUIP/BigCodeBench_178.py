
import re
import json
# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(ip_address):
    # Check if the provided IP address is valid
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'

    # Create a JSON response with the IP address
    json_response = {
        "public_ip": ip_address
    }

    # Return the public IP address from the JSON response
    return json_response['public_ip']