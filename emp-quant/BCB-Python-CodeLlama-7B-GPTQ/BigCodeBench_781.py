import os
from datetime import datetime
def task_func(filepath: str) -> dict:
    """
    Determine the size and date of the last modification of a file.
    The function should output with:
        dict: A dictionary containing the size (in bytes) and last modification
        date of the file in the format '%Y-%m-%d %H:%M:%S'.
    """
    file_stats = os.stat(filepath)
    file_size = file_stats.st_size
    file_mod_date = datetime.fromtimestamp(file_stats.st_mtime)
    return {
        'size': file_size,
        'mod_date': file_mod_date.strftime('%Y-%m-%d %H:%M:%S')
    }
filepath = 'path/to/file.txt'