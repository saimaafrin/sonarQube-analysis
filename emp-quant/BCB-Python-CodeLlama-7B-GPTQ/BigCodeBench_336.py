import re
import os
import glob
from pathlib import Path
def task_func(pattern, directory, extensions):
    """
    Find all files in a specific directory that contain a regex pattern in their contents in a case insensitive manner.
    The function should output with:
        list: A list of absolute file paths that contain the pattern.
    """
    # Create a list of all files in the directory
    files = glob.glob(os.path.join(directory, '*'))
    # Create a list of all file paths that contain the pattern
    file_paths = []
    for file in files:
        with open(file, 'r') as f:
            if re.search(pattern, f.read(), re.IGNORECASE):
                file_paths.append(file)
    return file_paths
pattern = 'python'
directory = '.'
extensions = ['py']