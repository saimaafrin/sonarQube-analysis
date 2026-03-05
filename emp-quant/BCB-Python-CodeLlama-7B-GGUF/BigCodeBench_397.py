
import re
import urllib.request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(API_URL):
    try:
        response = urllib.request.urlopen(API_URL)
        data = json.loads(response.read())
        ip_address = data['origin']
        if re.match(IP_REGEX, ip_address):
            return ip_address
        else:
            raise ValueError('Invalid IP address')
    except urllib.error.URLError as e:
        raise ValueError(f'API request failed: {e}')
    except json.decoder.JSONDecodeError as e:
        raise ValueError(f'Invalid JSON response: {e}')
    except ValueError as e:
        raise ValueError(f'Invalid IP address: {e}')