
import shutil
import pathlib
from typing import List, Tuple

def task_func(source_path: str, destination_path: str) -> Tuple[str, List[str]]:
    source_path = pathlib.Path(source_path)
    destination_path = pathlib.Path(destination_path)
    
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError("Source path does not exist or is not a directory.")
    
    copied_files = []
    for item in source_path.iterdir():
        if item.is_file():
            shutil.copy(item, destination_path)
            copied_files.append(item.name)
    
    return source_path.name, copied_files