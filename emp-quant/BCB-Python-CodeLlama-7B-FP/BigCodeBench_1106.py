from datetime import datetime
import os
from pathlib import Path
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(file_path):
    """
    Determine the creation time of a file and convert it to a formatted string '% Y-% m-% d% H:% M:% S'.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} does not exist.")
    creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
    return creation_time.strftime(DATE_FORMAT)