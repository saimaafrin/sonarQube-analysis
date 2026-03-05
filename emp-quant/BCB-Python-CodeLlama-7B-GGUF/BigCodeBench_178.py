
import re
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(ip_address):
    """
    Get the public IP address from a JSON response containing the IP address.

    Args:
        ip_address (str): The IP address to be validated.

    Returns:
        str: The public IP address.
    """
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'

    # Get the public IP address from the JSON response
    json_response = json.loads(ip_address)
    public_ip_address = json_response['ip']

    return public_ip_address