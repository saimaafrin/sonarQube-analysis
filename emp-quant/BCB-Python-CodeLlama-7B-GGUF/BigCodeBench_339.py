
import json
import urllib.parse
import hmac
import hashlib

def task_func(req_data, secret_key):
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")

    # Sign the request data with the secret key using HMAC SHA256
    signature = hmac.new(secret_key.encode(), json.dumps(req_data).encode(), hashlib.sha256).hexdigest()

    # URL encode the signature and replace spaces with '+'
    encoded_signature = urllib.parse.quote_plus(signature)

    return encoded_signature