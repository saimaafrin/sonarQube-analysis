
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
        raise FileNotFoundError(f"Directory {directory} does not exist")
    if not url.startswith('http'):
        raise TypeError(f"Invalid URL: {url}")

    status_codes = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        with open(file_path, 'rb') as f:
            file_data = f.read()
        metadata_json = json.dumps(metadata)
        response = requests.post(url, headers=HEADERS, data=file_data, params={'metadata': metadata_json})
        status_codes.append(response.status_code)
        time.sleep(1)

    return status_codes