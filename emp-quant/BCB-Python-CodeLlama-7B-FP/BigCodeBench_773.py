import os
import re
import shutil
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')
def task_func():
    for file in os.listdir(SOURCE_DIR):
        if FILE_PATTERN.match(file):
            prefix, suffix = file.split('-', 1)
            shutil.move(os.path.join(SOURCE_DIR, file), os.path.join(TARGET_DIR, prefix + '.json'))