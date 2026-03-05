
import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    result = []
    directory_path = Path(directory_path)
    if not os.path.exists(directory_path):
        raise ValueError("Directory does not exist")
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        file_stat = os.lstat(file_path)
        creation_time = datetime.fromtimestamp(file_stat.st_ctime)
        modification_time = datetime.fromtimestamp(file_stat.st_mtime)
        result.append((file, file_stat.st_size, creation_time, modification_time))
    return result