import requests
import json
import base64
def task_func(data, url="http://your-api-url.com"):
    # Convert the Python dictionary to a JSON-formatted string
    json_data = json.dumps(data)

    # Encode the JSON-formatted string in base64 format
    base64_data = base64.b64encode(json_data.encode("utf-8"))

    # Create a POST request with the base64-encoded payload
    response = requests.post(url, data=base64_data)

    # Return the response object received from the API endpoint
    return response
data = {"key1": "value1", "key2": "value2"}