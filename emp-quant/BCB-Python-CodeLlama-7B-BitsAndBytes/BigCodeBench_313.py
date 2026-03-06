
import re
import os
import shutil
from datetime import datetime

def task_func(directory):
    # Create a dictionary to store the files moved to each subdirectory
    subdirs = {}

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Get the full path of the file
        filepath = os.path.join(directory, filename)

        # Check if the file is a text file
        if os.path.isfile(filepath) and filename.endswith('.txt'):
            # Open the file and read its contents
            with open(filepath, 'r') as f:
                contents = f.read()

            # Use regular expressions to find the first text that is not enclosed in square brackets
            match = re.search(r'(?<!\[).*?(?!\])', contents)

            # If a match is found, move the file to a subdirectory with the same name
            if match:
                subdir_name = match.group(0)
                if subdir_name not in subdirs:
                    subdirs[subdir_name] = []
                subdirs[subdir_name].append(filename)
                shutil.move(filepath, os.path.join(directory, subdir_name, filename))

    # Return the directory path with organized files and the subdirectories dictionary
    return directory, subdirs