
import os
from datetime import datetime

def task_func(filepath: str) -> dict:
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    file_size = os.path.getsize(filepath)
    last_modified_timestamp = os.path.getmtime(filepath)
    last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    return {
        'size': file_size,
        'last_modified': last_modified_date
    }