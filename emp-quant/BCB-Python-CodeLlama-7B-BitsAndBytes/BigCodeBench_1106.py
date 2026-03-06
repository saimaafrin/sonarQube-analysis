
from datetime import datetime
import os
from pathlib import Path

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(file_path):
    file_path = Path(file_path)
    creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
    return creation_time.strftime(DATE_FORMAT)