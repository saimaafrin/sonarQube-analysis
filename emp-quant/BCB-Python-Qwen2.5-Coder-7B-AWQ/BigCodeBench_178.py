import re
import json
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
def task_func(ip_address):
    # Check if the provided IP address is valid
    if not re.match(IP_REGEX, ip_address):
        return 'Invalid IP address received'
    
    # Create a JSON response with the IP address
    json_response = json.dumps({'ip': ip_address})
    
    # Parse the JSON response
    parsed_json = json.loads(json_response)
    
    # Extract the public IP address from the JSON response
    public_ip = parsed_json['ip']
    
    return public_ip