import re
import json
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
def task_func(ip_address):
    """
    Get the public IP address from a JSON response containing the IP address.
    """
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'
    return ip_address