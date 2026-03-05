import os
from pathlib import Path
from datetime import datetime, timezone
def task_func(directory_path: str):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        raise ValueError("The provided directory does not exist.")
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each file in the directory
    for file_path in Path(directory_path).iterdir():
        if file_path.is_file():
            # Get the file size
            file_size = file_path.stat().st_size
            
            # Get the creation time and convert it to ISO format
            creation_time = datetime.fromtimestamp(file_path.stat().st_ctime, timezone.utc).isoformat()
            
            # Get the last modification time and convert it to ISO format
            modification_time = datetime.fromtimestamp(file_path.stat().st_mtime, timezone.utc).isoformat()
            
            # Append the file details as a tuple to the result list
            result.append((file_path.name, file_size, creation_time, modification_time))
    
    return result