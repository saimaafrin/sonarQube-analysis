
import os
from datetime import datetime

def task_func(filepath: str) -> dict:
    """
    Determine the size and date of the last modification of a file.

    Args:
        filepath (str): The path to the file.

    Returns:
        dict: A dictionary containing the size (in bytes) and last modification
            date of the file in the format '%Y-%m-%d %H:%M:%S'.
    """
    stat = os.stat(filepath)
    size = stat.st_size
    last_modified = datetime.fromtimestamp(stat.st_mtime)
    return {'size': size, 'last_modified': last_modified.strftime('%Y-%m-%d %H:%M:%S')}