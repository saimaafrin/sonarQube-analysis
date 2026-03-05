
import urllib.request
import os
import re
# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'
def task_func(url):
    # Download the file
    with urllib.request.urlopen(url) as response:
        with open(TARGET_FILE, 'wb') as f:
            f.write(response.read())
    # Search for occurrences of the word 'ERROR'
    with open(TARGET_FILE, 'r') as f:
        content = f.read()
        pattern = re.compile(SEARCH_PATTERN)
        occurrences = len(pattern.findall(content))
    return occurrences