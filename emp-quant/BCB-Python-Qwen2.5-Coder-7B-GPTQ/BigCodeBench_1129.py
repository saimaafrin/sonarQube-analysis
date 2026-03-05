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
        raise ValueError(f"Key '{unknown_key}' not found in JSON data")
    
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
    
    # Download the file from the URL
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        return os.path.abspath(save_path)
    else:
        raise Exception(f"Failed to download file from URL: {url}")
json_data = '{"url": "https://example.com/test.txt"}'
unknown_key = 'url'
save_dir = '/path/to/save/directory'