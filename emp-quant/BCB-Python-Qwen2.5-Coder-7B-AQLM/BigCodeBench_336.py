
import re
import os
import glob
from pathlib import Path

def task_func(pattern, directory, extensions):
    """
    Find all files in a specific directory that contain a regex pattern in their contents in a case insensitive manner.
    
    Args:
    pattern (str): The regex pattern to search for.
    directory (str): The directory to search in.
    extensions (list): A list of file extensions to search for.
    
    Returns:
    list: A list of absolute file paths that contain the pattern.
    """
    # Compile the regex pattern with case insensitivity
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Initialize a list to store the results
    results = []
    
    # Iterate over the specified extensions
    for ext in extensions:
        # Construct the glob pattern
        glob_pattern = os.path.join(directory, f'*.{ext}')
        
        # Use glob to find all files with the specified extension
        for file_path in glob.glob(glob_pattern):
            # Check if the file is a regular file
            if os.path.isfile(file_path):
                # Open the file and read its contents
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    # Check if the pattern is in the file content
                    if regex.search(content):
                        # If the pattern is found, add the absolute path to the results
                        results.append(Path(file_path).resolve())
    
    return results