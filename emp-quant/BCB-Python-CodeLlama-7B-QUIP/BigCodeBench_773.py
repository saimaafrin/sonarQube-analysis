
import os
import re
import shutil

# Constants
SOURCE_DIR = '/source/dir'
TARCE_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def task_func():
    for file in os.listdir(SOURCE_DIR):
        if FILE_PATTERN.match(file):
            file_name, file_ext = os.path.splitext(file)
            new_file_name = file_name + file_ext
            shutil.move(os.path.join(SOURCE_DIR, file), os.path.join(TARCE_DIR, new_file_name))
    return None