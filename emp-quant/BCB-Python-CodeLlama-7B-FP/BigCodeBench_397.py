import re
import urllib.request
import json
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
def task_func(API_URL):
    """
    Get the public IP address of the current host from an API.
    The function should raise the exception for:
        If the API request fails, the function will return the error message.
    The function should output with:
        str: The public IP address.
    """
    try:
        response = urllib.request.urlopen(API_URL)
        data = json.loads(response.read())
        ip_address = data['ip']
        if re.match(IP_REGEX, ip_address):
            return ip_address
        else:
            raise ValueError('Invalid IP address')
    except urllib.error.URLError as e:
        raise e
    except ValueError as e:
        raise e
API_URL = 'https://api.ipify.org?format=json'