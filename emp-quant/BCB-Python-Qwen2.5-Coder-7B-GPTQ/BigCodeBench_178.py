import re
import json
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
def task_func(ip_address):
    # Check if the provided IP address is valid
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'
    
    # Assume the JSON response is a dictionary with a key 'ip'
    json_response = {'ip': ip_address}
    
    # Extract the public IP address from the JSON response
    public_ip = json_response.get('ip', 'Invalid IP address received')
    
    return public_ip