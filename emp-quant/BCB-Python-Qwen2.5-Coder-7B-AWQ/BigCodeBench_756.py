import shutil
from pathlib import Path
from typing import List
def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Check if source_dir and target_dir exist
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError("source_dir does not exist")
    if not target_path.exists() or not target_path.is_dir():
        raise ValueError("target_dir does not exist")
    
    moved_count = 0
    
    # Iterate through all files in the source directory
    for file_path in source_path.iterdir():
        if file_path.is_file() and file_path.suffix in extensions:
            # Move the file to the target directory
            shutil.move(file_path, target_path / file_path.name)
            moved_count += 1
    
    return moved_count