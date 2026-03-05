
import re
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(ip_address):
    # Check if the provided IP address is valid
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'

    # Get the public IP address
    public_ip_address = ip_address

    return public_ip_address