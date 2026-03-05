
import re
import urllib.request
import json
# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(API_URL):
    try:
        with urllib.request.urlopen(API_URL) as response:
            data = response.read()
            json_data = json.loads(data)
            ip_address = json_data.get('ip')
            if ip_address and re.match(IP_REGEX, ip_address):
                return ip_address
            else:
                raise ValueError("Invalid IP address format")
    except urllib.error.URLError as e:
        return str(e.reason)
    except json.JSONDecodeError as e:
        return str(e)