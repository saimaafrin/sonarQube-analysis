import re
import os
import glob
def task_func(directory, word):
    """
    Count the number of files in a directory that contain a specific word.
    """
    count = 0
    for file in glob.glob(os.path.join(directory, '*')):
        with open(file, 'r') as f:
            if re.search(word, f.read()):
                count += 1
    return count