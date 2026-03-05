import os
from datetime import datetime
def task_func(filepath: str) -> dict:
    # Check if the file exists
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    # Get the size of the file
    file_size = os.path.getsize(filepath)
    
    # Get the last modification time of the file
    last_modified_timestamp = os.path.getmtime(filepath)
    
    # Convert the timestamp to a readable date format
    last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    # Return the size and last modification date in a dictionary
    return {'size': file_size, 'last_modified': last_modified_date}