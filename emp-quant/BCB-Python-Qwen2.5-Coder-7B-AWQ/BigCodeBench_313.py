import re
import os
import shutil
from datetime import datetime
def task_func(directory):
    # Dictionary to store the files organized by their first non-bracketed text
    organized_files = {}
    # Regex pattern to find the first text not enclosed in square brackets
    pattern = re.compile(r'(?<!\[)\b\w+\b(?![\]])')

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Search for the pattern in the filename
            match = pattern.search(filename)
            if match:
                # Get the first non-bracketed text
                key = match.group(0)
                # Create the subdirectory if it doesn't exist
                if key not in organized_files:
                    organized_files[key] = []
                # Move the file to the subdirectory
                shutil.move(file_path, os.path.join(directory, key, filename))
                organized_files[key].append(filename)

    # Return the directory path and the dictionary of organized files
    return directory, organized_files