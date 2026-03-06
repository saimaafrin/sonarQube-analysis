
import re
import urllib.request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(API_URL):
    try:
        response = urllib.request.urlopen(API_URL)
        data = response.read().decode('utf-8')
        ip_info = json.loads(data)
        public_ip = ip_info['ip']
        
        # Validate the IP address using regex
        if re.match(IP_REGEX, public_ip):
            return public_ip
        else:
            raise ValueError("Invalid IP address format")
    
    except urllib.error.URLError as e:
        return f"API request failed: {e.reason}"
    except json.JSONDecodeError as e:
        return f"Failed to decode JSON response: {e.msg}"
    except KeyError as e:
        return f"Expected key 'ip' not found in response"