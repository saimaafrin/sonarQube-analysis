import re
import json
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
def task_func(ip_address):
    # Check if the provided IP address is valid
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'
    
    # Return the valid IP address
    return ip_address