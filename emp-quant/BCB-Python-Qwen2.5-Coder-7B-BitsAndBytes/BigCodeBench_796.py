
import os
import re

BRACKET_PATTERN = r'[(){}\\[\]]'

def task_func(directory):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.search(BRACKET_PATTERN, file):
                matching_files.append(os.path.join(root, file))
    return matching_files