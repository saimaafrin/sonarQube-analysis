
import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    if not source_path.exists():
        raise ValueError(f"Source directory {source_dir} does not exist.")
    if not target_path.exists():
        raise ValueError(f"Target directory {target_dir} does not exist.")
    
    moved_count = 0
    
    for item in source_path.iterdir():
        if item.is_file() and item.suffix in extensions:
            item.rename(target_path / item.name)
            moved_count += 1
    
    return moved_count