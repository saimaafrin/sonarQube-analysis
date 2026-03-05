
import re
import urllib.request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(API_URL):
    try:
        response = urllib.request.urlopen(API_URL)
        data = json.loads(response.read())
        ip_address = re.search(IP_REGEX, data['ip_address'])
        return ip_address.group(0)
    except Exception as e:
        raise e