import os
import ctypes
from datetime import datetime
import pytz
def task_func(filepath):
    """
    Loads a DLL file from the specified filepath and returns its metadata, including creation time, modification time, and file size.
    The times are displayed in UTC format.
    This function demonstrates the use of ctypes for loading DLLs and os module for accessing file metadata.
    """
    # Load the DLL file
    dll_handle = ctypes.CDLL(filepath)

    # Get the file metadata
    file_metadata = os.stat(filepath)

    # Convert the file times to UTC format
    creation_time = datetime.fromtimestamp(file_metadata.st_ctime, tz=pytz.utc)
    modification_time = datetime.fromtimestamp(file_metadata.st_mtime, tz=pytz.utc)

    # Create a dictionary with the metadata
    metadata = {
        'Creation Time': creation_time,
        'Modification Time': modification_time,
        'Size': file_metadata.st_size
    }

    # Return the DLL name and the metadata dictionary
    return filepath, metadata
filepath = 'path/to/my/dll.dll'