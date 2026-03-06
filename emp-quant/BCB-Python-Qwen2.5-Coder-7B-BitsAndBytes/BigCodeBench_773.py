
import os
import re
import shutil

# Constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def task_func():
    # Ensure the target directory exists
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # Iterate over all files in the source directory
    for filename in os.listdir(SOURCE_DIR):
        match = FILE_PATTERN.match(filename)
        if match:
            prefix = match.group(1)
            new_filename = f"{prefix}.json"
            old_file_path = os.path.join(SOURCE_DIR, filename)
            new_file_path = os.path.join(TARGET_DIR, new_filename)
            shutil.move(old_file_path, new_file_path)

task_func()