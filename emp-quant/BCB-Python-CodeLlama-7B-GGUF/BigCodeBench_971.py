
import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory {directory_path} does not exist")

    directory = Path(directory_path)
    files = [f for f in directory.iterdir() if f.is_file()]

    result = []
    for file in files:
        file_size = file.stat().st_size
        creation_time = datetime.fromtimestamp(file.stat().st_ctime, timezone.utc)
        modification_time = datetime.fromtimestamp(file.stat().st_mtime, timezone.utc)
        result.append((file.name, file_size, creation_time.isoformat(), modification_time.isoformat()))

    return result

result = task_func('/path/to/empty_directory')
print(result)