
import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    result = []
    directory = Path(directory_path)
    
    if not directory.exists():
        raise ValueError("The provided directory does not exist.")
    
    for file_path in directory.iterdir():
        if file_path.is_file():
            file_size = file_path.stat().st_size
            creation_time = datetime.fromtimestamp(file_path.stat().st_ctime, timezone.utc).isoformat()
            modification_time = datetime.fromtimestamp(file_path.stat().st_mtime, timezone.utc).isoformat()
            result.append((file_path.name, file_size, creation_time, modification_time))
    
    return result