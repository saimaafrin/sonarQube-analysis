import re
import os
import shutil
from datetime import datetime
def task_func(directory):
    # Dictionary to store files organized by their first non-bracketed text
    organized_files = {}
    # Regex pattern to find text not enclosed in square brackets
    pattern = re.compile(r'[^[\]]+')

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Open and read the file
            with open(file_path, 'r') as f:
                content = f.read()
                # Find the first non-bracketed text
                match = pattern.search(content)
                if match:
                    key = match.group(0).strip()
                    # Create subdirectory if it doesn't exist
                    if key not in organized_files:
                        subdirectory_path = os.path.join(root, key)
                        os.makedirs(subdirectory_path, exist_ok=True)
                        organized_files[key] = []
                    # Move the file to the subdirectory
                    shutil.move(file_path, os.path.join(subdirectory_path, file))
                    organized_files[key].append(file)

    # Return the directory path and the dictionary of organized files
    return directory, organized_files