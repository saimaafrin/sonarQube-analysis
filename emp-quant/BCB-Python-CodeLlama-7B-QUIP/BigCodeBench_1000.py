
import urllib.request
import os
import json
import pandas as pd
# Constants
TARGET_JSON_FILE = "downloaded_file.json"
def task_func(url):
    # Download the JSON file
    with urllib.request.urlopen(url) as response:
        with open(TARGET_JSON_FILE, "wb") as file:
            file.write(response.read())
    # Read the JSON file and convert it to a DataFrame
    with open(TARGET_JSON_FILE, "r") as file:
        data = json.load(file)
        df = pd.DataFrame(data)
    # Delete the temporary JSON file
    os.remove(TARGET_JSON_FILE)
    return df