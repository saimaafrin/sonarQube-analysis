import re
import os
import glob
def task_func(directory, word):
    # Initialize the count of files containing the word
    count = 0
    
    # Use glob to find all files in the directory
    files = glob.glob(os.path.join(directory, '*'))
    
    # Iterate over each file in the directory
    for file in files:
        # Check if the file is a regular file
        if os.path.isfile(file):
            # Open the file in read mode
            with open(file, 'r') as f:
                # Read the content of the file
                content = f.read()
                # Use regular expression to find the word in the content
                if re.search(r'\b' + re.escape(word) + r'\b', content):
                    # Increment the count if the word is found
                    count += 1
    
    # Return the count of files containing the word
    return count