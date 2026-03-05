import re
import os
import glob
from pathlib import Path
def task_func(pattern, directory, extensions):
    # Initialize an empty list to store the file paths
    matching_files = []
    
    # Create a regular expression pattern with case insensitivity
    regex_pattern = re.compile(pattern, re.IGNORECASE)
    
    # Use glob to find all files in the specified directory with the given extensions
    for ext in extensions:
        for file_path in glob.glob(os.path.join(directory, f'*.{ext}')):
            # Check if the file is a regular file and not a directory
            if os.path.isfile(file_path):
                # Open the file and read its contents
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    # Check if the regex pattern is found in the file content
                    if regex_pattern.search(content):
                        # If found, add the absolute file path to the list
                        matching_files.append(Path(file_path).resolve())
    
    # Return the list of matching file paths
    return matching_files