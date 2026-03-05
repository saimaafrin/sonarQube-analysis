
import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    # Check if the provided directory exists
    if not os.path.exists(directory_path):
        raise ValueError("The provided directory does not exist.")
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each file in the directory
    for file_name in os.listdir(directory_path):
        # Construct the full file path
        file_path = os.path.join(directory_path, file_name)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file size in bytes
            file_size = os.path.getsize(file_path)
            
            # Get the creation time and convert it to UTC
            creation_time = datetime.fromtimestamp(os.path.getctime(file_path), timezone.utc).isoformat()
            
            # Get the last modification time and convert it to UTC
            modification_time = datetime.fromtimestamp(os.path.getmtime(file_path), timezone.utc).isoformat()
            
            # Append the file information as a tuple to the result list
            result.append((file_name, file_size, creation_time, modification_time))
    
    return result