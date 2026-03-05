
import os
from pathlib import Path
import shutil

def task_func(kwargs, target_dir="non_none_files"):
    copied_files = []
    for file_path, content in kwargs.items():
        if os.path.exists(file_path) and content:
            target_path = Path(target_dir) / file_path
            target_path.parent.mkdir(exist_ok=True)
            shutil.copy(file_path, target_path)
            copied_files.append(target_path.resolve())
    return copied_files