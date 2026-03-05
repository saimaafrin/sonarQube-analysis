
import os
import re

BRACKET_PATTERN = '[(){}\\[\\]]'

def task_func(directory):
    """
    Finds all files in the specified directory whose names contain any type of bracket.
    
    :param directory: str - The path to the directory to search.
    :return: list[str] - A list of file paths that contain brackets in their names.
    """
    bracket_files = []
    for filename in os.listdir(directory):
        if re.search(BRACKET_PATTERN, filename):
            bracket_files.append(os.path.join(directory, filename))
    return bracket_files