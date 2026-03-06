
import re
import os
import glob
from pathlib import Path

def task_func(pattern, directory, extensions):
    # Create a list to store the file paths
    file_paths = []

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Check if the file has the desired pattern in its contents
        if re.search(pattern, open(file, 'r').read(), re.IGNORECASE):
            # Add the file path to the list
            file_paths.append(os.path.join(directory, file))

    # Return the list of file paths
    return file_paths

print(task_func(pattern, directory, extensions))