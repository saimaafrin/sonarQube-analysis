
import os
import re
import shutil

# Constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def task_func():
    # Iterate over all files in the source directory
    for file in os.listdir(SOURCE_DIR):
        # Check if the file matches the file pattern
        match = FILE_PATTERN.match(file)
        if match:
            # Extract the prefix part of the filename
            prefix = match.group(1)
            # Rename the file
            shutil.move(os.path.join(SOURCE_DIR, file), os.path.join(TARGET_DIR, prefix + '.json'))