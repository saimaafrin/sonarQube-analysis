
import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    if not Path(source_dir).exists():
        raise ValueError("Source directory does not exist")
    if not Path(target_dir).exists():
        raise ValueError("Target directory does not exist")

    moved_files = 0
    for file in Path(source_dir).iterdir():
        if file.suffix in extensions:
            shutil.move(file, target_dir)
            moved_files += 1

    return moved_files