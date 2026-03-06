
import requests
import json
import base64

def task_func(data, url="http://your-api-url.com"):
    # Convert the dictionary to a JSON-formatted string
    json_data = json.dumps(data)
    
    # Encode the JSON string in base64 format
    encoded_data = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    
    # Create a payload dictionary
    payload = {
        'payload': encoded_data
    }
    
    # Send a POST request to the API endpoint
    response = requests.post(url, json=payload)
    
    return response