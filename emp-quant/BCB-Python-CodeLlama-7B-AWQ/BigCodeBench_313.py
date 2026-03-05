import re
import os
import shutil
from datetime import datetime
def task_func(directory):
    """
    Organize files in a directory based on the first text that is not enclosed in square brackets.
    Move the files to subdirectories named after this text. If no matching text is found, the file is not moved.
    """
    # Create a dictionary to store the files moved to each subdirectory
    files_moved = {}

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Get the full file path
        filepath = os.path.join(directory, filename)

        # Check if the file is a regular file
        if os.path.isfile(filepath):
            # Open the file and read its contents
            with open(filepath, 'r') as f:
                contents = f.read()

            # Find the first text that is not enclosed in square brackets
            match = re.search(r'\[([^\]]+)\]', contents)

            # If a match was found, move the file to a subdirectory with the same name
            if match:
                subdir = match.group(1)
                if not os.path.exists(os.path.join(directory, subdir)):
                    os.makedirs(os.path.join(directory, subdir))
                shutil.move(filepath, os.path.join(directory, subdir))
                files_moved.setdefault(subdir, []).append(filename)

    # Return the directory path with organized files and the files moved to each subdirectory
    return directory, files_moved
directory = 'path/to/directory'