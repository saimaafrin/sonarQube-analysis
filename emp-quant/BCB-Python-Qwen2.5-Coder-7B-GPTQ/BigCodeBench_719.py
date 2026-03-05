import re
import os
import glob
def task_func(directory, word):
    count = 0
    # Use glob to find all files in the directory
    files = glob.glob(os.path.join(directory, '*'))
    for file in files:
        # Check if the file is a text file
        if file.endswith('.txt'):
            with open(file, 'r') as f:
                # Read the content of the file
                content = f.read()
                # Use regular expression to find the word in the content
                if re.search(r'\b' + re.escape(word) + r'\b', content):
                    count += 1
    return count