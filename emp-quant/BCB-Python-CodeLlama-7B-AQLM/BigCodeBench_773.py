import os
import re
import shutil
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')
def task_func():
    """
    Move all json files in a source directory to a target directory and rename them by splitting the filename the last time "-" occurs and keeping the prefix part of the filename.
    
    Parameters:
    - None

    Returns:
    - None

    Requirements:
    - os
    - re
    - shutil

    Example:
    >>> task_func()

    """
    # Get all files in the source directory
    files = os.listdir(SOURCE_DIR)

    # Iterate over all files
    for file in files:
        # Check if the file is a json file
        if file.endswith('.json'):
            # Split the filename by the last time "-" occurs
            filename_parts = FILE_PATTERN.split(file)

            # Check if the filename has been split
            if len(filename_parts) == 3:
                # Move the file to the target directory
                shutil.move(os.path.join(SOURCE_DIR, file), os.path.join(TARGET_DIR, filename_parts[0] + '.json'))