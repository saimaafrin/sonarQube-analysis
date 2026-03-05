
import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    if not source_path.exists():
        raise ValueError("Source directory does not exist.")
    if not target_path.exists():
        raise ValueError("Target directory does not exist.")

    moved_count = 0

    for file_path in source_path.iterdir():
        if file_path.is_file() and file_path.suffix in extensions:
            target_path.joinpath(file_path.name).symlink_to(file_path)
            moved_count += 1

    return moved_count