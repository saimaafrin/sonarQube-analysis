import requests
import os
import json
import time
HEADERS = {
    'accept': 'text/json',
    'Content-Type': 'application/json'
}
def task_func(url, directory, metadata):
    """
    Upload all files from a specific directory to the specified server URL, along with the associated metadata.
    In addition, the speed limit function pauses for one second after each upload.
    The function should raise the exception for:
        - The function will raise FileNotFoundError if the directory does not exist.
        - The function will raise TypeError if the url is invalid.
    The function should output with:
        - list: A list of status codes for the upload responses.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist.")

    # Check if the url is valid
    if not url.startswith("http"):
        raise TypeError(f"Invalid url: {url}")

    # Initialize the list of status codes
    status_codes = []

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Get the file path
        file_path = os.path.join(directory, file)

        # Check if the file exists
        if not os.path.exists(file_path):
            continue

        # Open the file
        with open(file_path, "rb") as f:
            # Read the file content
            file_content = f.read()

        # Create the metadata dictionary
        metadata_dict = {
            "name": file,
            "size": os.path.getsize(file_path),
            "type": "application/octet-stream"
        }

        # Merge the metadata dictionary with the metadata
        metadata_dict.update(metadata)

        # Create the request data
        request_data = {
            "file": file_content,
            "metadata": metadata_dict
        }

        # Send the request
        response = requests.post(url, headers=HEADERS, data=json.dumps(request_data))

        # Add the status code to the list
        status_codes.append(response.status_code)

        # Pause for one second
        time.sleep(1)

    # Return the list of status codes
    return status_codes
url = "https://example.com/upload"
directory = "path/to/directory"
metadata = {
    "key1": "value1",
    "key2": "value2"
}