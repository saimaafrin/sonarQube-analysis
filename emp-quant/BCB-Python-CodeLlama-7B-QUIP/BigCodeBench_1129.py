
import json
import requests
import os
from datetime import datetime

def task_func(json_data, unknown_key, save_dir=None):
    # Parse the JSON data to find the URL associated with the specified key
    url = json_data[unknown_key]

    # Download the file from the URL
    response = requests.get(url)

    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')

    # Create the filename for the downloaded file
    filename = f'{unknown_key}_{timestamp}.txt'

    # Determine the directory to save the file in
    if save_dir:
        directory = save_dir
    else:
        directory = os.getcwd()

    # Save the file to the specified directory
    with open(os.path.join(directory, filename), 'wb') as f:
        f.write(response.content)

    # Return the absolute path of the downloaded file
    return os.path.join(directory, filename)