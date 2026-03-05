import re
import os
import glob
def task_func(directory, word):
    """
    Count the number of files in a directory that contain a specific word.

    Args:
        directory (str): The directory to search.
        word (str): The word to search for.

    Returns:
        count (int): The number of files that contain the given word.
    """
    count = 0
    for filename in glob.iglob(os.path.join(directory, '*')):
        with open(filename, 'r') as f:
            if re.search(word, f.read()):
                count += 1
    return count