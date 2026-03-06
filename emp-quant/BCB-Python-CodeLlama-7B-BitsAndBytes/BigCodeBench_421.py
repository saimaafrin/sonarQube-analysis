
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
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    # Check if the url is valid
    if not url.startswith('http'):
        raise TypeError(f"Invalid URL: {url}")

    # Create a list to store the status codes
    status_codes = []

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Open the file and read its contents
        with open(os.path.join(directory, file), 'rb') as f:
            file_data = f.read()

        # Create a dictionary with the file metadata
        file_metadata = {
            'name': file,
            'size': len(file_data),
            'type': 'application/octet-stream'
        }

        # Merge the file metadata with the global metadata
        metadata = {**metadata, **file_metadata}

        # Upload the file to the server
        response = requests.post(url, data=file_data, headers=HEADERS, json=metadata)

        # Pause for one second after each upload
        time.sleep(1)

        # Add the status code to the list
        status_codes.append(response.status_code)

    # Return the list of status codes
    return status_codes