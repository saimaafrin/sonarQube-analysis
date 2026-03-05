import re
import os
import glob
def task_func(directory, word):
    count = 0
    # Use glob to find all files in the directory
    files = glob.glob(os.path.join(directory, '*'))
    for file in files:
        # Check if the file is a regular file
        if os.path.isfile(file):
            # Open the file and read its contents
            with open(file, 'r') as f:
                content = f.read()
                # Use regular expression to find the word in the content
                if re.search(r'\b' + re.escape(word) + r'\b', content):
                    count += 1
    return count