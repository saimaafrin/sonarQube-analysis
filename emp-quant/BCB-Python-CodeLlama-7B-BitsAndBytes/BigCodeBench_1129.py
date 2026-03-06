
import json
import requests
import os
from datetime import datetime

def task_func(json_data, unknown_key, save_dir=None):
    # Parse the JSON data to find the URL associated with the specified key
    data = json.loads(json_data)
    url = data[unknown_key]

    # Download the file from the URL
    response = requests.get(url)

    # Create a timestamped filename for the downloaded file
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    filename = f'{unknown_key}_{timestamp}.txt'

    # Save the file to the specified directory or current working directory
    if save_dir:
        filepath = os.path.join(save_dir, filename)
    else:
        filepath = os.path.join(os.getcwd(), filename)

    with open(filepath, 'wb') as f:
        f.write(response.content)

    return filepath

filepath = task_func(json_data, unknown_key, save_dir)
print(filepath)