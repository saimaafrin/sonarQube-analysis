
import re
import os
import glob

def task_func(directory, word):
    count = 0
    for filename in glob.glob(os.path.join(directory, '*')):
        if filename.endswith('.txt'):
            with open(filename, 'r') as file:
                if re.search(r'\b' + re.escape(word) + r'\b', file.read()):
                    count += 1
    return count