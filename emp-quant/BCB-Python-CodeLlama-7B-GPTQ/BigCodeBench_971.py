import os
from pathlib import Path
from datetime import datetime, timezone
def task_func(directory_path: str):
    """
    Analyzes a given directory, listing each file it contains along with its size, creation time, and last modification time without recursing into subdirectories.
    """
    if not os.path.exists(directory_path):
        raise ValueError("The provided directory does not exist.")

    directory_path = Path(directory_path)
    file_list = []
    for file in directory_path.iterdir():
        if file.is_file():
            file_size = file.stat().st_size
            creation_time = datetime.fromtimestamp(file.stat().st_ctime, timezone.utc)
            modification_time = datetime.fromtimestamp(file.stat().st_mtime, timezone.utc)
            file_list.append((file.name, file_size, creation_time.isoformat(), modification_time.isoformat()))

    return file_list