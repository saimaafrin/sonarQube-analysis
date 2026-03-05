
from datetime import datetime
import os
from pathlib import Path
# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(file_path):
    """
    Determine the creation time of a file and convert it to a formatted string '%Y-%m-%d %H:%M:%S'.
    
    :param file_path: str, the path to the file
    :return: str, the creation time of the file in the format '%Y-%m-%d %H:%M:%S'
    """
    # Ensure the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Get the creation time of the file
    creation_time = Path(file_path).stat().st_ctime
    
    # Convert the creation time to a formatted string
    formatted_time = datetime.fromtimestamp(creation_time).strftime(DATE_FORMAT)
    
    return formatted_time