
import urllib.request
import os
import re

# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'

def task_func(url):
    # Download the file
    with urllib.request.urlopen(url) as response:
        with open(TARGET_FILE, 'wb') as file:
            file.write(response.read())

    # Search for occurrences of the word 'ERROR'
    with open(TARGET_FILE, 'r') as file:
        text = file.read()
        occurrences = len(re.findall(SEARCH_PATTERN, text))

    # Print the result
    print(f'Occurrences: {occurrences}')

# Call the function with the URL of the file to download
task_func('https://example.com/file.txt')