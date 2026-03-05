import re
import os
import shutil
from datetime import datetime
def task_func(directory):
    """
    Organize files in a directory based on the first text that is not enclosed in square brackets.
    Move the files to subdirectories named after this text. If no matching text is found, the file is not moved.
    """
    # Create a dictionary to store the files and their corresponding subdirectories
    files_dict = {}

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Get the file path
        file_path = os.path.join(directory, file)

        # Check if the file is a regular file
        if os.path.isfile(file_path):
            # Open the file and read its contents
            with open(file_path, 'r') as f:
                contents = f.read()

            # Use regular expressions to find the first text that is not enclosed in square brackets
            match = re.search(r'(?<!\[)\w+', contents)

            # If a match is found, create a subdirectory with the matching text
            if match:
                subdir = match.group()
                if subdir not in files_dict:
                    files_dict[subdir] = []

                # Move the file to the subdirectory
                shutil.move(file_path, os.path.join(directory, subdir))
                files_dict[subdir].append(file)

    # Return the directory path with organized files and the files dictionary
    return directory, files_dict
directory = 'path/to/directory'