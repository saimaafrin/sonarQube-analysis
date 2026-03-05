
import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)

    if not source_dir.exists():
        raise ValueError(f"Source directory {source_dir} does not exist.")
    if not target_dir.exists():
        raise ValueError(f"Target directory {target_dir} does not exist.")

    moved_count = 0

    for ext in extensions:
        for file in source_dir.glob(f"*.{ext}"):
            shutil.move(file, target_dir)
            moved_count += 1

    return moved_count