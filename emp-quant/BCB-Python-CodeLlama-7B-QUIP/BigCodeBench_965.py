
import os
import re
import shutil

def task_func(source_directory: str, target_directory: str, pattern: str = r"\d{4}") -> int:
    if not os.path.exists(source_directory) or not os.path.isdir(source_directory):
        return 0
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    files = [f for f in os.listdir(source_directory) if re.match(pattern, f)]
    for file in files:
        shutil.move(os.path.join(source_directory, file), os.path.join(target_directory, file))
    return len(files)