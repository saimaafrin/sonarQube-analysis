import os
import re
BRACKET_PATTERN = '[(){}\\[\\]]'
def task_func(directory):
    """
    Finds all files in the specified directory whose names contain any type of bracket (round, curly, or square).

    Args:
    directory (str): The directory to search for files.

    Returns:
    list[str]: A list of file paths that contain brackets in their names.
    """
    bracket_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.search(BRACKET_PATTERN, file):
                bracket_files.append(os.path.join(root, file))
    return bracket_files