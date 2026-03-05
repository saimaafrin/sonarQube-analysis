
import os
from datetime import datetime
def task_func(filepath: str) -> dict:
    # Check if the file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    # Get the size of the file
    size = os.path.getsize(filepath)
    
    # Get the last modification time of the file
    last_mod_time = os.path.getmtime(filepath)
    
    # Convert the last modification time to a readable date format
    last_mod_date = datetime.fromtimestamp(last_mod_time).strftime('%Y-%m-%d %H:%M:%S')
    
    # Return the size and last modification date as a dictionary
    return {'size': size, 'last_mod_date': last_mod_date}