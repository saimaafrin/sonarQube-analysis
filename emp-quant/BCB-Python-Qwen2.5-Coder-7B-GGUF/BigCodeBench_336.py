
import re
import os
import glob
from pathlib import Path

def task_func(pattern, directory, extensions):
    """
    Find all files in a specific directory that contain a regex pattern in their contents in a case insensitive manner.
    
    :param pattern: The regex pattern to search for.
    :param directory: The directory to search in.
    :param extensions: A list of file extensions to search for.
    :return: A list of absolute file paths that contain the pattern.
    """
    # Compile the regex pattern with case insensitivity
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Initialize a list to store the results
    results = []
    
    # Iterate over the specified extensions
    for ext in extensions:
        # Create a glob pattern to match files with the specified extension
        glob_pattern = os.path.join(directory, f'*.{ext}')
        
        # Find all files that match the glob pattern
        for file_path in glob.glob(glob_pattern):
            # Check if the file is a regular file
            if os.path.isfile(file_path):
                # Open the file and read its contents
                with open(file_path, 'r', encoding='utf-8') as file:
                    contents = file.read()
                    
                    # Check if the regex pattern is found in the file contents
                    if regex.search(contents):
                        # Add the absolute file path to the results list
                        results.append(Path(file_path).resolve())
    
    # Return the list of absolute file paths that contain the pattern
    return results