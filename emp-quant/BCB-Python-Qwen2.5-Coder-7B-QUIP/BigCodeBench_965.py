
import os
import re
import shutil

def task_func(source_directory: str, target_directory: str, pattern: str = r"\d{4}") -> int:
    # Check if source_directory exists and is a directory
    if not os.path.exists(source_directory) or not os.path.isdir(source_directory):
        return 0

    # Check if target_directory exists, if not, create it
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Initialize a counter for the number of files moved
    files_moved = 0

    # Iterate over all files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the file matches the regex pattern
        if re.match(pattern, filename):
            # Construct the full file path
            source_file = os.path.join(source_directory, filename)
            # Construct the target file path
            target_file = os.path.join(target_directory, filename)
            # Move the file to the target directory
            shutil.move(source_file, target_file)
            # Increment the counter
            files_moved += 1

    # Return the number of files moved
    return files_moved