
import urllib.request
import os
import re

# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'

def task_func(url):
    # Download the file from the specified URL
    urllib.request.urlretrieve(url, TARGET_FILE)
    
    # Initialize a counter for occurrences
    occurrences = 0
    
    # Open the downloaded file and search for the pattern
    with open(TARGET_FILE, 'r') as file:
        for line in file:
            occurrences += len(re.findall(SEARCH_PATTERN, line, re.IGNORECASE))
    
    # Clean up by removing the downloaded file
    os.remove(TARGET_FILE)
    
    return occurrences