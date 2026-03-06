
import re
import urllib.request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(API_URL):
    try:
        with urllib.request.urlopen(API_URL) as response:
            data = json.loads(response.read())
            ip_address = data['origin']
            if re.match(IP_REGEX, ip_address):
                return ip_address
            else:
                raise ValueError('Invalid IP address')
    except urllib.error.URLError as e:
        return 'API request failed: ' + str(e)