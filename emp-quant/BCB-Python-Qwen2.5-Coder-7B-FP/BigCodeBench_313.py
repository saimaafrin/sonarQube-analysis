import re
import os
import shutil
from datetime import datetime
def task_func(directory):
    # Dictionary to store files organized by their first non-bracketed text
    organized_files = {}
    # Regex to find the first text not enclosed in square brackets
    pattern = re.compile(r'(?<!\[)\b\w+\b(?![^\]]*\])')

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Find the first non-bracketed text in the file name
            match = pattern.search(file)
            if match:
                key = match.group(0)
                if key not in organized_files:
                    organized_files[key] = []
                # Move the file to the corresponding subdirectory
                new_dir = os.path.join(root, key)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                shutil.move(file_path, os.path.join(new_dir, file))
                organized_files[key].append(file)

    # Return the directory path and the dictionary of organized files
    return directory, organized_files