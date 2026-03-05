
from datetime import datetime
import os
from pathlib import Path
# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(file_path):
    """
    Determine the creation time of a file and convert it to a formatted string '%Y-%m-%d %H:%M:%S'.
    
    Args:
    file_path (str): The path to the file.
    
    Returns:
    str: The creation time of the file in the format '%Y-%m-%d %H:%M:%S'.
    """
    # Convert the file path to a Path object
    path = Path(file_path)
    
    # Get the creation time of the file
    creation_time = path.stat().st_ctime
    
    # Convert the creation time to a datetime object
    creation_datetime = datetime.fromtimestamp(creation_time)
    
    # Format the datetime object to the specified string format
    formatted_time = creation_datetime.strftime(DATE_FORMAT)
    
    return formatted_time