
import urllib.request
import os
import re
# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'
def task_func(url):
    # Download the file from the URL
    urllib.request.urlretrieve(url, TARGET_FILE)
    
    # Open the file and read the content
    with open(TARGET_FILE, 'r') as file:
        content = file.read()
    
    # Search for the word 'ERROR' using regex
    occurrences = len(re.findall(SEARCH_PATTERN, content, re.IGNORECASE))
    
    # Clean up the downloaded file
    os.remove(TARGET_FILE)
    
    return occurrences