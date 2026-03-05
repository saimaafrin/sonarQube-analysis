
import json
import urllib.parse
import hmac
import hashlib

def task_func(req_data, secret_key):
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")
    
    # Convert the dictionary to a sorted JSON string
    json_str = json.dumps(req_data, sort_keys=True)
    
    # Create a new HMAC object using the secret key and SHA256
    hmac_obj = hmac.new(secret_key.encode(), json_str.encode(), hashlib.sha256)
    
    # Get the hexadecimal representation of the HMAC digest
    hmac_hex = hmac_obj.hexdigest()
    
    # URL encode the HMAC signature and replace spaces with '+'
    url_encoded_hmac = urllib.parse.quote(hmac_hex).replace('%20', '+')
    
    return url_encoded_hmac