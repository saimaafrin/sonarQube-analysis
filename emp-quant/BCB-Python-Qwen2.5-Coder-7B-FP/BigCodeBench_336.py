import re
import os
import glob
from pathlib import Path
def task_func(pattern, directory, extensions):
    # Initialize an empty list to store the file paths
    matching_files = []
    
    # Create a regex pattern that matches any of the specified extensions
    extension_pattern = r'\.(' + '|'.join(extensions) + r')$'
    
    # Use glob to find all files in the directory with the specified extensions
    for file_path in glob.glob(os.path.join(directory, '**', '*'), recursive=True):
        # Check if the file has one of the specified extensions
        if re.search(extension_pattern, file_path, re.IGNORECASE):
            # Open the file and read its contents
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                contents = file.read()
                # Check if the pattern is in the file contents, case-insensitively
                if re.search(pattern, contents, re.IGNORECASE):
                    # If the pattern is found, add the file path to the list
                    matching_files.append(file_path)
    
    # Return the list of file paths that contain the pattern
    return matching_files