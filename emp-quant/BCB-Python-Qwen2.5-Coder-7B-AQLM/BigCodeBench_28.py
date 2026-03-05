
import requests
import json
import base64

def task_func(data, url="http://your-api-url.com"):
    # Convert the Python dictionary to a JSON-formatted string
    json_data = json.dumps(data)
    
    # Encode the JSON string in base64 format
    base64_data = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    
    # Create a payload dictionary with the base64-encoded data
    payload = {'payload': base64_data}
    
    # Send a POST request to the API endpoint with the payload
    response = requests.post(url, json=payload)
    
    return response