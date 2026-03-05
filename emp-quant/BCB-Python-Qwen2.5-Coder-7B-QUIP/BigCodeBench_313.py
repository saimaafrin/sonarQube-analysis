
import re
import os
import shutil
from datetime import datetime

def task_func(directory):
    # Define the regular expression to find the first text not enclosed in square brackets
    pattern = re.compile(r'\[([^\[\]]+)\]')
    subdirectory_map = {}
    moved_files = []

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Search for the pattern in the file name
            match = pattern.search(file)
            if match:
                # Get the text before the first square bracket
                subdirectory_name = match.group(1)
                # Create the subdirectory if it does not exist
                if subdirectory_name not in subdirectory_map:
                    subdirectory_map[subdirectory_name] = []
                    os.makedirs(os.path.join(root, subdirectory_name))
                # Move the file to the subdirectory
                shutil.move(os.path.join(root, file), os.path.join(root, subdirectory_name, file))
                moved_files.append(file)
            else:
                # If no match, add the file to the list of moved files
                moved_files.append(file)
    
    # Return the directory path with organized files and the dictionary of moved files
    return (directory, subdirectory_map)