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
        ip = data['ip']
        if re.match(IP_REGEX, ip):
            return ip
        else:
            raise Exception('Invalid IP address')
    except Exception as e:
        return str(e)
API_URL = 'https://api.ipify.org?format=json'