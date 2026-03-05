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
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")

    file_size = os.path.getsize(filepath)
    last_mod_time = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M:%S')

    return {'size': file_size, 'last_mod_date': last_mod_time}