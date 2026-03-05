
import re
import os
import glob
from pathlib import Path

def task_func(pattern, directory, extensions):
    # Create a list of all files in the directory
    files = [str(f) for f in Path(directory).iterdir()]

    # Filter the list to only files with the specified extensions
    files = [f for f in files if f.endswith(extensions)]

    # Create a list of all files that contain the pattern in their contents
    matching_files = [f for f in files if re.search(pattern, f)]

    return matching_files