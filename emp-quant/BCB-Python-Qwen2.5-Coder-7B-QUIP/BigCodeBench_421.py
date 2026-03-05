
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
    
    # Check if the URL is valid
    if not isinstance(url, str) or not url.startswith('http'):
        raise TypeError("Invalid URL")
    
    # Initialize a list to store status codes
    status_codes = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            data = file.read()
        
        # Prepare the payload with metadata
        payload = {
            'filename': filename,
            'data': data,
            'metadata': metadata
        }
        
        # Send the POST request
        response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
        
        # Append the status code to the list
        status_codes.append(response.status_code)
        
        # Pause for one second
        time.sleep(1)
    
    # Return the list of status codes
    return status_codes