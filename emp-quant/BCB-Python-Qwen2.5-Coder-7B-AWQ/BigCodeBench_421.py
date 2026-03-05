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
    if not url.startswith('http'):
        raise TypeError("The URL is invalid.")
    
    status_codes = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            # Open the file and read its content
            with open(file_path, 'rb') as file:
                file_content = file.read()
            
            # Create a dictionary to hold the file and metadata
            data = {
                'file': file_content,
                'metadata': metadata
            }
            
            # Convert the dictionary to JSON
            json_data = json.dumps(data)
            
            # Send a POST request to the server
            response = requests.post(url, headers=HEADERS, data=json_data)
            
            # Append the status code to the list
            status_codes.append(response.status_code)
            
            # Pause for one second
            time.sleep(1)
    
    return status_codes