
import re
import os
import glob
from pathlib import Path

def task_func(pattern, directory, extensions):
    """
    Find all files in a specific directory that contain a regex pattern in their contents in a case insensitive manner.
    
    :param pattern: Regex pattern to search for
    :param directory: Directory to search within
    :param extensions: List of file extensions to consider
    :return: List of absolute file paths that contain the pattern
    """
    # Compile the regex pattern in a case-insensitive manner
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Initialize an empty list to store the results
    matching_files = []
    
    # Iterate over the specified extensions
    for ext in extensions:
        # Construct the full path pattern
        path_pattern = os.path.join(directory, f'*.{ext}')
        
        # Use glob to find all files with the specified extension
        files = glob.glob(path_pattern)
        
        # Check each file for the pattern
        for file_path in files:
            try:
                # Open and read the file content
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    # Search for the pattern in the file content
                    if regex.search(content):
                        # If found, add the absolute file path to the list
                        matching_files.append(Path(file_path).resolve())
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
    return matching_files