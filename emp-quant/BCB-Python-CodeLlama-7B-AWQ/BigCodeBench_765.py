import os
from pathlib import Path
import shutil
def task_func(kwargs, target_dir="non_none_files"):
    copied_files = []
    for file in kwargs:
        file_path = Path(file)
        if file_path.exists() and file_path.stat().st_size > 0:
            shutil.copy(file_path, target_dir)
            copied_files.append(file_path)
    return copied_files
kwargs = [
    "file1.txt",
    "file2.txt",
    "file3.txt",
    "file4.txt",
    "file5.txt",
]
target_dir = "non_none_files"