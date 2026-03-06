
import os
import ctypes
from datetime import datetime
import pytz

def task_func(filepath):
    # Load the DLL file using ctypes
    dll_handle = ctypes.CDLL(filepath)

    # Get the metadata of the DLL file
    creation_time = datetime.fromtimestamp(os.stat(filepath).st_ctime, tz=pytz.utc)
    modification_time = datetime.fromtimestamp(os.stat(filepath).st_mtime, tz=pytz.utc)
    file_size = os.stat(filepath).st_size

    # Create a dictionary with the metadata
    metadata = {
        'Creation Time': creation_time,
        'Modification Time': modification_time,
        'Size': file_size
    }

    # Return the name of the loaded DLL file and the metadata dictionary
    return filepath, metadata