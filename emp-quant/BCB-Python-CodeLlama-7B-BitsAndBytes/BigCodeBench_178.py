
import re
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(ip_address):
    # Check if the IP address is valid
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'

    # Get the public IP address from the JSON response
    json_data = json.loads(ip_address)
    public_ip = json_data['ip']

    # Return the public IP address
    return public_ip