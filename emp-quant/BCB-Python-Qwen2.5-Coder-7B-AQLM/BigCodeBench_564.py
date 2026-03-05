
import os
import ctypes
from datetime import datetime
import pytz

def task_func(filepath):
    # Load the DLL file
    dll = ctypes.CDLL(filepath)
    
    # Get the metadata of the DLL file
    creation_time = os.path.getctime(filepath)
    modification_time = os.path.getmtime(filepath)
    file_size = os.path.getsize(filepath)
    
    # Convert the times to UTC format
    utc_tz = pytz.utc
    creation_time_utc = datetime.fromtimestamp(creation_time, utc_tz)
    modification_time_utc = datetime.fromtimestamp(modification_time, utc_tz)
    
    # Create a dictionary with the metadata
    metadata = {
        'Creation Time': creation_time_utc,
        'Modification Time': modification_time_utc,
        'Size': file_size
    }
    
    # Return the name of the loaded DLL file and the metadata
    return os.path.basename(filepath), metadata