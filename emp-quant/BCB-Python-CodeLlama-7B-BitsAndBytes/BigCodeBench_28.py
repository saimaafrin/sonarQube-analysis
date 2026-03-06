
import requests
import json
import base64

def task_func(data, url="http://your-api-url.com"):
    # Convert the Python dictionary to a JSON-formatted string
    json_str = json.dumps(data)

    # Encode the JSON string in base64 format
    base64_str = base64.b64encode(json_str.encode("utf-8"))

    # Create a POST request with the base64-encoded JSON payload
    response = requests.post(url, data=base64_str)

    # Return the response object
    return response