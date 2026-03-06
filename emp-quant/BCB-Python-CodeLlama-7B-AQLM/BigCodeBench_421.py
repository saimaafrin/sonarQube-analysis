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

    Parameters:
    url (str): The server URL.
    directory (str): The directory containing the files to be uploaded.
    metadata (dict): The metadata to be associated with the files.

    Returns:
    list: A list of status codes for the upload responses.

    Requirements:
    - requests
    - os
    - json
    - time

    Raises:
    - The function will raise FileNotFoundError if the directory does not exist.
    - The function will raise TypeError if the url is invalid.

    Example:
    >>> task_func('https://www.example.com', './uploads', {'userId': 'abc'})
    """

    if not os.path.exists(directory):
        raise FileNotFoundError('The directory does not exist.')

    if not url.startswith('http'):
        raise TypeError('The url is invalid.')

    # Create a list to store the status codes
    status_codes = []

    # Iterate through the files in the directory
    for file in os.listdir(directory):
        # Open the file
        with open(os.path.join(directory, file), 'rb') as f:
            # Upload the file
            r = requests.post(url, headers=HEADERS, data=f, params=metadata)
            # Append the status code to the list
            status_codes.append(r.status_code)
            # Pause for one second
            time.sleep(1)

    # Return the list of status codes
    return status_codes