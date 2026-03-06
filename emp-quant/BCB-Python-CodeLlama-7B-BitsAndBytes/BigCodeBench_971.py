
import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    """
    Analyzes a given directory, listing each file it contains along with its size, creation time, and last modification time without recursing into subdirectories.

    :param directory_path: The path to the directory to analyze.
    :return: A list of tuples, where each tuple contains (file name, file size in bytes, creation time in ISO format, modification time in ISO format).
    """
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory {directory_path} does not exist.")

    directory_path = Path(directory_path)
    file_list = []
    for file in directory_path.iterdir():
        if file.is_file():
            file_list.append((file.name, file.stat().st_size, file.stat().st_ctime, file.stat().st_mtime))

    return file_list

result = task_func('/path/to/empty_directory')
print(result)