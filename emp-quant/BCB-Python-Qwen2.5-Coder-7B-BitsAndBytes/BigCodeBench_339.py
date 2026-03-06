
import json
import urllib.parse
import hmac
import hashlib

def task_func(req_data, secret_key):
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")
    
    # Convert the dictionary to a sorted JSON string
    req_json = json.dumps(req_data, sort_keys=True)
    
    # Encode the JSON string and the secret key as bytes
    req_bytes = req_json.encode('utf-8')
    secret_bytes = secret_key.encode('utf-8')
    
    # Create an HMAC SHA256 hash object
    hmac_obj = hmac.new(secret_bytes, req_bytes, hashlib.sha256)
    
    # Get the hexadecimal representation of the digest
    hex_digest = hmac_obj.hexdigest()
    
    # URL encode the hexadecimal digest and replace spaces with '+'
    url_encoded_signature = urllib.parse.quote(hex_digest).replace('%20', '+')
    
    return url_encoded_signature