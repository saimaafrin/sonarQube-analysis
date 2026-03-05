
import re
import os
import glob
from pathlib import Path

def task_func(pattern, directory, extensions):
    # Compile the regex pattern for case insensitive matching
    pattern = re.compile(pattern, re.IGNORECASE)
    
    # Initialize a list to store the file paths
    matching_files = []
    
    # Iterate over the specified extensions
    for ext in extensions:
        # Construct the glob pattern to match files with the given extension
        glob_pattern = os.path.join(directory, f'*.{ext}')
        
        # Find all files that match the glob pattern
        for file_path in glob.glob(glob_pattern):
            # Check if the file is a file and not a directory
            if os.path.isfile(file_path):
                # Open the file and read its contents
                with open(file_path, 'r') as file:
                    content = file.read()
                    
                    # Check if the pattern matches the content
                    if pattern.search(content):
                        # Add the file path to the list if it matches the pattern
                        matching_files.append(file_path)
    
    # Return the list of matching file paths
    return matching_files