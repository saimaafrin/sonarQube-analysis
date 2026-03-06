
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
        raise FileNotFoundError("Directory does not exist")
    
    # Validate the URL
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise TypeError(f"Invalid URL: {e}")
    
    status_codes = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Read the file content
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            # Create the payload
            payload = {
                "filename": filename,
                "content": file_data.decode('utf-8'),
                "metadata": metadata
            }
            
            # Send the POST request
            response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
            status_codes.append(response.status_code)
            
            # Pause for 1 second
            time.sleep(1)
    
    return status_codes