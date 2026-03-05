import urllib.request
import os
import re
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'
def task_func(url):
    # Download the file
    with urllib.request.urlopen(url) as response:
        with open(TARGET_FILE, 'wb') as f:
            f.write(response.read())

    # Search for occurrences of the word "ERROR"
    with open(TARGET_FILE, 'r') as f:
        text = f.read()
        occurrences = len(re.findall(SEARCH_PATTERN, text))

    # Print the result
    print(f'Occurrences: {occurrences}')
url = 'https://www.example.com/file.txt'