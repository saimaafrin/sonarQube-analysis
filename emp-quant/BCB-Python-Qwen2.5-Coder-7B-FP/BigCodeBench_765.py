import os
from pathlib import Path
import shutil
def task_func(kwargs, target_dir="non_none_files"):
    copied_files = []
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)

    for file_path, content in kwargs.items():
        source_path = Path(file_path)
        if source_path.exists() and content:
            target_file_path = target_path / source_path.name
            shutil.copy2(source_path, target_file_path)
            copied_files.append(str(target_file_path))

    return copied_files