
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
        raise FileNotFoundError("The directory does not exist")
    # Create a list to store the status codes
    status_codes = []
    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Get the file path
        file_path = os.path.join(directory, file)
        # Get the file metadata
        file_metadata = metadata.get(file_path, {})
        # Upload the file
        response = requests.post(url, files={'file': open(file_path, 'rb')}, headers=HEADERS, json=file_metadata)
        # Add the status code to the list
        status_codes.append(response.status_code)
        # Pause for one second
        time.sleep(1)
    # Return the list of status codes
    return status_codes