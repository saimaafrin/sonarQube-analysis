
import os
import re

BRACKET_PATTERN = '[(){}\\[\\]]'

def task_func(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(BRACKET_PATTERN, file):
                file_paths.append(os.path.join(root, file))
    return file_paths