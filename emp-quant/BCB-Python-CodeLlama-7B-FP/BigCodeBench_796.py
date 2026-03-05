import os
import re
BRACKET_PATTERN = '[(){}\\[\\]]'
def task_func(directory):
    """
    Finds all files in the specified directory whose names contain any type of bracket (round, curly, or square).
    Uses an internal constant BRACKET_PATTERN = '[(){}\\[\\]]', which specifies the brackets that are looked for.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(BRACKET_PATTERN, file):
                file_paths.append(os.path.join(root, file))
    return file_paths