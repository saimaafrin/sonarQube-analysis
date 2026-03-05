
import os
import re

BRACKET_PATTERN = '[(){}\\[\\]]'

def task_func(directory):
    files = []
    for file in os.listdir(directory):
        if re.search(BRACKET_PATTERN, file):
            files.append(os.path.join(directory, file))
    return files