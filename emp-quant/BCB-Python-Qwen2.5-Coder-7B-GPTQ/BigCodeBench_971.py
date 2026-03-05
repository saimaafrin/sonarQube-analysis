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
    for file in os.listdir(directory_path):
        # Construct the full file path
        file_path = os.path.join(directory_path, file)
        
        # Check if it is a file and not a directory
        if os.path.isfile(file_path):
            # Get file size
            file_size = os.path.getsize(file_path)
            
            # Get creation time and convert to UTC ISO format
            creation_time = datetime.fromtimestamp(os.path.getctime(file_path), timezone.utc).isoformat()
            
            # Get modification time and convert to UTC ISO format
            modification_time = datetime.fromtimestamp(os.path.getmtime(file_path), timezone.utc).isoformat()
            
            # Append the file details as a tuple to the result list
            result.append((file, file_size, creation_time, modification_time))
    
    # Return the list of tuples
    return result