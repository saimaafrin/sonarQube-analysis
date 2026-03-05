import json
import requests
import os
from datetime import datetime
def task_func(json_data, unknown_key, save_dir=None):
    # Parse the JSON data
    data = json.loads(json_data)
    
    # Retrieve the URL associated with the specified key
    url = data.get(unknown_key)
    
    if not url:
        raise ValueError(f"Key '{unknown_key}' not found in JSON data.")
    
    # Download the file from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Generate a timestamped filename
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    filename = f"{unknown_key}_{timestamp}.txt"
    
    # Determine the save directory
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        save_path = os.path.join(save_dir, filename)
    else:
        save_path = os.path.join(os.getcwd(), filename)
    
    # Save the file
    with open(save_path, 'wb') as file:
        file.write(response.content)
    
    # Return the absolute path of the saved file
    return os.path.abspath(save_path)