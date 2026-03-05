
import re
import os
import glob

def task_func(directory, word):
    count = 0
    for file in glob.glob(directory + '/*'):
        if re.search(word, open(file).read()):
            count += 1
    return count