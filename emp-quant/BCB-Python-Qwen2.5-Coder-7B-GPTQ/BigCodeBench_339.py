import json
import urllib.parse
import hmac
import hashlib
def task_func(req_data, secret_key):
    # Check if req_data is a dictionary
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(req_data)
    
    # Create a new HMAC object using SHA256 and the secret key
    hmac_obj = hmac.new(secret_key.encode(), json_data.encode(), hashlib.sha256)
    
    # Get the hexadecimal representation of the HMAC digest
    hmac_signature = hmac_obj.hexdigest()
    
    # URL encode the signature and replace spaces with '+'
    url_encoded_signature = urllib.parse.quote_plus(hmac_signature)
    
    return url_encoded_signature