import shutil
from pathlib import Path
from typing import List
def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    # Check if source_dir and target_dir exist
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError("source_dir does not exist or is not a directory")
    if not target_path.exists() or not target_path.is_dir():
        raise ValueError("target_dir does not exist or is not a directory")

    moved_files_count = 0

    # Iterate over all files in the source directory
    for file in source_path.iterdir():
        if file.is_file() and file.suffix in extensions:
            # Move the file to the target directory
            shutil.move(file, target_path / file.name)
            moved_files_count += 1

    return moved_files_count