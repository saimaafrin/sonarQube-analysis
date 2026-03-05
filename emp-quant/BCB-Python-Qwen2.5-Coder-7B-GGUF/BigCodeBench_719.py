
import re
import os
import glob

def task_func(directory, word):
    count = 0
    # Use glob to find all files in the directory
    for file_path in glob.glob(os.path.join(directory, '*')):
        # Check if the path is a file
        if os.path.isfile(file_path):
            # Open the file and read its contents
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Check if the word is in the content
                if re.search(r'\b' + re.escape(word) + r'\b', content):
                    count += 1
    return count