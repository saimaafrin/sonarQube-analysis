import os
from pathlib import Path
import shutil
def task_func(kwargs, target_dir="non_none_files"):
    copied_files = []
    target_dir_path = Path(target_dir)
    target_dir_path.mkdir(parents=True, exist_ok=True)

    for file_path, content in kwargs.items():
        source_path = Path(file_path)
        if source_path.exists() and content:
            target_path = target_dir_path / source_path.name
            shutil.copy2(source_path, target_path)
            copied_files.append(str(target_path))

    return copied_files