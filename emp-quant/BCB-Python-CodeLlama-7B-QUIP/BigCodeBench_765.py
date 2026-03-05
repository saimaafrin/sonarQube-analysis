
import os
from pathlib import Path
import shutil

def task_func(kwargs, target_dir="non_none_files"):
    copied_files = []
    for file in kwargs["files"]:
        if os.path.exists(file) and os.path.getsize(file) > 0:
            shutil.copy(file, target_dir)
            copied_files.append(file)
    return copied_files