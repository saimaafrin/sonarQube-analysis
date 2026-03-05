import urllib.request
import os
import re
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'
def task_func(url):
    # Download the file from the URL
    urllib.request.urlretrieve(url, TARGET_FILE)
    
    # Initialize a counter for occurrences
    occurrences = 0
    
    # Open the downloaded file and read line by line
    with open(TARGET_FILE, 'r') as file:
        for line in file:
            # Use regular expression to find all occurrences of the pattern
            matches = re.findall(SEARCH_PATTERN, line)
            # Increment the counter by the number of matches found
            occurrences += len(matches)
    
    # Clean up by removing the downloaded file
    os.remove(TARGET_FILE)
    
    # Return the total number of occurrences
    return occurrences