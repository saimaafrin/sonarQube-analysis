import os
import ctypes
from datetime import datetime
import pytz
def task_func(filepath):
    # Load the DLL file using ctypes
    dll = ctypes.CDLL(filepath)
    
    # Get the file metadata using os module
    file_stat = os.stat(filepath)
    
    # Convert times to UTC format
    creation_time_utc = datetime.fromtimestamp(file_stat.st_ctime, pytz.utc)
    modification_time_utc = datetime.fromtimestamp(file_stat.st_mtime, pytz.utc)
    
    # Create a dictionary with the metadata
    metadata = {
        'Creation Time': creation_time_utc,
        'Modification Time': modification_time_utc,
        'Size': file_stat.st_size
    }
    
    # Return the DLL name and the metadata dictionary
    return os.path.basename(filepath), metadata