import urllib.request
import os
import re
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'
def task_func(url):
    # Download the text file from the specified URL
    urllib.request.urlretrieve(url, TARGET_FILE)
    
    # Initialize a counter for occurrences of the word 'ERROR'
    occurrences = 0
    
    # Open the downloaded file and search for the word 'ERROR'
    with open(TARGET_FILE, 'r') as file:
        for line in file:
            # Find all occurrences of the word 'ERROR' in the current line
            matches = re.findall(SEARCH_PATTERN, line)
            # Increment the counter by the number of matches found
            occurrences += len(matches)
    
    # Remove the downloaded file after processing
    os.remove(TARGET_FILE)
    
    # Return the total number of occurrences of the word 'ERROR'
    return occurrences