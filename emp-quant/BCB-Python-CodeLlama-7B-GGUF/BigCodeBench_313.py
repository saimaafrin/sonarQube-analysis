
import re
import os
import shutil
from datetime import datetime

def task_func(directory):
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
            match = re.search(r'\[?([^\[\]]+)\]?', contents)

            # If a match is found, move the file to a subdirectory with the same name
            if match:
                subdir_name = match.group(1)
                subdir_path = os.path.join(directory, subdir_name)

                # Create the subdirectory if it does not exist
                if not os.path.isdir(subdir_path):
                    os.makedirs(subdir_path)

                # Move the file to the subdirectory
                shutil.move(file_path, subdir_path)

                # Add the file to the dictionary
                if subdir_name not in files_dict:
                    files_dict[subdir_name] = []
                files_dict[subdir_name].append(file)

    # Return the directory path with organized files and the files dictionary
    return directory, files_dict