
import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    if not Path(directory_path).exists():
        raise ValueError("The provided directory does not exist.")
    
    result = []
    for file_path in Path(directory_path).iterdir():
        if file_path.is_file():
            file_size = file_path.stat().st_size
            creation_time = datetime.fromtimestamp(file_path.stat().st_ctime, tz=timezone.utc).isoformat()
            modification_time = datetime.fromtimestamp(file_path.stat().st_mtime, tz=timezone.utc).isoformat()
            result.append((file_path.name, file_size, creation_time, modification_time))
    
    return result