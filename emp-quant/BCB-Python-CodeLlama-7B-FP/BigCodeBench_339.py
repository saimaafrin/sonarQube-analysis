import json
import urllib.parse
import hmac
import hashlib
def task_func(req_data, secret_key):
    """
    Signs the specified request data with a secret key using HMAC SHA256, then URL encodes the signature and replaces spaces with '+'.
    """
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")

    # Convert the request data to a JSON string
    req_data_json = json.dumps(req_data)

    # Create a HMAC signature of the request data using the secret key
    signature = hmac.new(secret_key.encode(), req_data_json.encode(), hashlib.sha256).hexdigest()

    # URL encode the signature and replace spaces with '+'
    signature_urlencoded = urllib.parse.quote_plus(signature)

    return signature_urlencoded
req_data = {"key1": "value1", "key2": "value2"}
secret_key = "secret_key"