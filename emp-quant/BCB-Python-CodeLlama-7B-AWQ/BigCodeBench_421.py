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
        raise FileNotFoundError(f"Directory {directory} does not exist")

    # Check if the url is valid
    if not url.startswith("http"):
        raise TypeError(f"Invalid URL: {url}")

    # Initialize the list of status codes
    status_codes = []

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Get the file path
        file_path = os.path.join(directory, file)

        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist")

        # Open the file
        with open(file_path, "rb") as f:
            # Read the file contents
            file_contents = f.read()

        # Create the metadata dictionary
        metadata_dict = {
            "name": file,
            "metadata": metadata
        }

        # Convert the metadata dictionary to JSON
        metadata_json = json.dumps(metadata_dict)

        # Make the upload request
        response = requests.post(url, headers=HEADERS, data=file_contents, json=metadata_json)

        # Check the response status code
        status_code = response.status_code
        status_codes.append(status_code)

        # Pause for one second
        time.sleep(1)

    # Return the list of status codes
    return status_codes
url = "https://example.com/upload"
directory = "path/to/directory"
metadata = {"key": "value"}