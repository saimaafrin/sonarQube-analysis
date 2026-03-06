
import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    # Convert input strings to Path objects
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    # Check if source and target directories exist
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError("Source directory does not exist.")
    if not target_path.exists() or not target_path.is_dir():
        raise ValueError("Target directory does not exist.")

    # Initialize counter for moved files
    moved_files_count = 0

    # Iterate over each file in the source directory
    for item in source_path.iterdir():
        if item.is_file() and item.suffix.lower() in extensions:
            # Move the file to the target directory
            shutil.move(item, target_path / item.name)
            moved_files_count += 1

    return moved_files_count