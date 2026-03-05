import requests
import os
import json
import time
HEADERS = {
    'accept': 'text/json',
    'Content-Type': 'application/json'
}
def task_func(url, directory, metadata):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError("The directory does not exist.")
    
    # Check if the URL is valid
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise TypeError("Invalid URL.") from e
    
    status_codes = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            # Read the file content
            with open(file_path, 'rb') as file:
                file_content = file.read()
            
            # Create the payload
            payload = {
                'file': (filename, file_content),
                'metadata': metadata
            }
            
            # Send the POST request
            response = requests.post(url, headers=HEADERS, files=payload)
            status_codes.append(response.status_code)
            
            # Pause for one second
            time.sleep(1)
    
    return status_codes