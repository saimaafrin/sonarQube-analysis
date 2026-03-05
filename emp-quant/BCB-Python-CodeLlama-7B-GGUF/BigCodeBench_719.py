
import re
import os
import glob

def task_func(directory, word):
    # Create a list of all files in the directory
    files = glob.glob(os.path.join(directory, '*'))

    # Initialize the count to 0
    count = 0

    # Iterate over the files and check if the word is present
    for file in files:
        with open(file, 'r') as f:
            if re.search(word, f.read()):
                count += 1

    return count