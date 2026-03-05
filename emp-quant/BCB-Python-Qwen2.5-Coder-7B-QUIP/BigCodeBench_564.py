
import os
import ctypes
from datetime import datetime
import pytz

def task_func(filepath):
    # Load the DLL file
    dll = ctypes.CDLL(filepath)
    
    # Get the metadata of the DLL file
    creation_time = datetime.fromtimestamp(os.path.getctime(filepath), pytz.utc)
    modification_time = datetime.fromtimestamp(os.path.getmtime(filepath), pytz.utc)
    size = os.path.getsize(filepath)
    
    # Return the name of the loaded DLL file and its metadata
    return {
        'str': os.path.basename(filepath),
        'dict': {
            'Creation Time': creation_time,
            'Modification Time': modification_time,
            'Size': size
        }
    }