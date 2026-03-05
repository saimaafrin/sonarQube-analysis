
import re
import os
import glob
from pathlib import Path

def task_func(pattern, directory, extensions):
    """
    Find all files in a specific directory that contain a regex pattern in their contents in a case insensitive manner.

    Args:
        pattern (str): The regex pattern to search for.
        directory (str): The directory to search in.
        extensions (list[str]): A list of file extensions to search for.

    Returns:
        list: A list of absolute file paths that contain the pattern.
    """
    # Create a list of all files in the directory
    files = glob.glob(os.path.join(directory, '*'))

    # Create a list of all files that match the extensions
    matching_files = [file for file in files if file.endswith(tuple(extensions))]

    # Create a list of all files that contain the pattern in their contents
    containing_files = []
    for file in matching_files:
        with open(file, 'r') as f:
            if re.search(pattern, f.read(), re.IGNORECASE):
                containing_files.append(file)

    return containing_files