
import os
from datetime import datetime

def task_func(filepath: str) -> dict:
    """
    Determine the size and date of the last modification of a file.
    :param filepath: The path to the file
    :return: A dictionary containing the size (in bytes) and last modification
    date of the file in the format '%Y-%m-%d %H:%M:%S'
    """
    try:
        file_info = os.stat(filepath)
        last_modified = datetime.fromtimestamp(file_info.st_mtime)
        size = file_info.st_size
    except FileNotFoundError:
        last_modified = None
        size = None
    return {
        'last_modified': last_modified,
        'size': size
    }