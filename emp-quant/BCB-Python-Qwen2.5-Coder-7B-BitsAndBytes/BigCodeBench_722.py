
import urllib.request
import os
import re

# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'

def task_func(url):
    # Download the file from the URL
    urllib.request.urlretrieve(url, TARGET_FILE)
    
    # Initialize the count of occurrences
    occurrences = 0
    
    # Open the downloaded file and read its contents
    with open(TARGET_FILE, 'r') as file:
        content = file.read()
        
        # Use regular expression to find all occurrences of the pattern
        matches = re.findall(SEARCH_PATTERN, content)
        
        # Count the number of matches
        occurrences = len(matches)
    
    # Remove the downloaded file after processing
    os.remove(TARGET_FILE)
    
    return occurrences