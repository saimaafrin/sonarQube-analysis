
import urllib.request
import os
import json
import pandas as pd

# Constants
TARGET_JSON_FILE = "downloaded_file.json"

def task_func(url):
    # Download the JSON file
    urllib.request.urlretrieve(url, TARGET_JSON_FILE)

    # Read the JSON file and convert it to a pandas DataFrame
    with open(TARGET_JSON_FILE, "r") as f:
        data = json.load(f)
        df = pd.DataFrame(data)

    # Delete the temporary JSON file
    os.remove(TARGET_JSON_FILE)

    return df