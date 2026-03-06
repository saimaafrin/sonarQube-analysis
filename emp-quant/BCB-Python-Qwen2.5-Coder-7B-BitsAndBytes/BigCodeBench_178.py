
import re
import json

# Constants
IP_REGEX = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'

def task_func(json_response):
    # Extract IP address from JSON response
    ip_address = json.loads(json_response).get('ip', '')
    
    # Validate IP address
    if re.match(IP_REGEX, ip_address):
        return ip_address
    else:
        return 'Invalid IP address received'