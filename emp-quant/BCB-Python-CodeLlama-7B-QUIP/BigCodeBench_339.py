
import json
import urllib.parse
import hmac
import hashlib

def task_func(req_data, secret_key):
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")
    hmac_signature = hmac.new(secret_key, req_data.encode(), hashlib.sha256).digest()
    return urllib.parse.quote_plus(hmac_signature.hexdigest())