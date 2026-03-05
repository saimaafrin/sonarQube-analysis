
import json
import requests
import os
from datetime import datetime

def task_func(json_data, unknown_key, save_dir=None):
    # Parse the JSON data to find the URL associated with the specified key
    url = json.loads(json_data).get(unknown_key)
    if not url:
        raise ValueError(f"Key {unknown_key} not found in JSON data")

    # Download the file from the URL
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to download file from {url}")

    # Save the file with a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = f"{unknown_key}_{timestamp}.txt"
    if save_dir:
        filepath = os.path.join(save_dir, filename)
    else:
        filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath