
import requests
import os
import json
import time

# Redefining the function in the current context
HEADERS = {
    'accept': 'text/json',
    'Content-Type': 'application/json'
}

def task_func(url, directory, metadata):
    if not os.path.exists(directory):
        raise FileNotFoundError("The directory does not exist.")
    
    if not url.startswith('http'):
        raise TypeError("The URL is invalid.")
    
    status_codes = []
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                files = {'file': (filename, file)}
                response = requests.post(url, headers=HEADERS, files=files, data=json.dumps(metadata))
                status_codes.append(response.status_code)
                time.sleep(1)
    
    return status_codes