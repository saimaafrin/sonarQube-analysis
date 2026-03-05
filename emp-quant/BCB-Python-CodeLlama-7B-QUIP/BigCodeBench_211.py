
import requests
import os
import zipfile

def task_func(url, destination_directory, headers=None):
    # Download the zip file
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Extract the zip file to the specified directory
        with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
            zf.extractall(destination_directory)
        # Return the list of extracted files
        return os.listdir(destination_directory)
    else:
        return []