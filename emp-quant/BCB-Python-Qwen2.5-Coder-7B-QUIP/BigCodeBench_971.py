
import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    # Check if the directory exists
    if not Path(directory_path).is_dir():
        raise ValueError("The provided directory does not exist.")
    
    # Initialize an empty list to store the results
    result = []
    
    # List all files in the directory
    for file_name in os.listdir(directory_path):
        # Get the full path of the file
        file_path = Path(directory_path) / file_name
        
        # Get the file size
        file_size = file_path.stat().st_size
        
        # Get the creation time
        creation_time = datetime.fromtimestamp(file_path.stat().st_birthtime, timezone.utc).isoformat()
        
        # Get the modification time
        modification_time = datetime.fromtimestamp(file_path.stat().st_mtime, timezone.utc).isoformat()
        
        # Append the tuple to the result list
        result.append((file_name, file_size, creation_time, modification_time))
    
    return result