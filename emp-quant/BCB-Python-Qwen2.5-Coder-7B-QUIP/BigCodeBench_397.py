
import re
import urllib.request
import json
# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(API_URL):
    try:
        with urllib.request.urlopen(API_URL) as response:
            data = json.loads(response.read().decode('utf-8'))
            public_ip = data['ip']
            if re.match(IP_REGEX, public_ip):
                return public_ip
            else:
                raise ValueError("Invalid public IP address")
    except Exception as e:
        return str(e)