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
        raise FileNotFoundError("The specified directory does not exist.")
    
    # Check if the URL is valid
    if not url.startswith('http'):
        raise TypeError("The provided URL is invalid.")
    
    status_codes = []
    
    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            # Open the file and read its content
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            # Prepare the payload with file data and metadata
            payload = {
                'file': (filename, file_data),
                'metadata': metadata
            }
            
            # Send the POST request to the server
            response = requests.post(url, headers=HEADERS, files=payload)
            
            # Append the status code to the list
            status_codes.append(response.status_code)
            
            # Pause for one second after each upload
            time.sleep(1)
    
    return status_codes