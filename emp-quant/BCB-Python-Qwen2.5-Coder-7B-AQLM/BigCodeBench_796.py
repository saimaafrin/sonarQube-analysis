
import os
import re

BRACKET_PATTERN = '[(){}\\[\\]]'

def task_func(directory):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(BRACKET_PATTERN, file):
                matching_files.append(os.path.join(root, file))
    return matching_files