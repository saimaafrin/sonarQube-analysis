import urllib.request
import os
import re
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'
def task_func(url):
    """
    Download a text file from the specified url and search for occurrences of the word "ERROR."

    Parameters:
    - url (str): The url of the text file to be downloaded.

    Returns:
    - occurrences (int): The number of occurrences of the word 'ERROR'.

    Requirements:
    - urllib
    - os
    - re

    Example:
    >>> task_func('http://example.com/log.txt')
    5 # Assuming there are 5 occurrences of 'ERROR' in the file
    """
    # Download the file
    urllib.request.urlretrieve(url, TARGET_FILE)

    # Open the file
    with open(TARGET_FILE, 'r') as f:
        # Read the file
        file_content = f.read()

        # Search for occurrences of the word 'ERROR'
        occurrences = len(re.findall(SEARCH_PATTERN, file_content))

    # Delete the file
    os.remove(TARGET_FILE)

    return occurrences