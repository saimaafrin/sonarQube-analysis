import os
import ctypes
from datetime import datetime
import pytz
def task_func(filepath):
    """
    Loads a DLL file from the specified filepath and returns its metadata, including creation time, modification time, and file size. The times are displayed in UTC format.
    This function demonstrates the use of ctypes for loading DLLs and os module for accessing file metadata.
    """
    # Load the DLL file
    dll = ctypes.CDLL(filepath)

    # Get the file metadata
    file_metadata = os.stat(filepath)

    # Convert the file metadata to UTC format
    creation_time = datetime.fromtimestamp(file_metadata.st_ctime, tz=pytz.utc)
    modification_time = datetime.fromtimestamp(file_metadata.st_mtime, tz=pytz.utc)
    file_size = file_metadata.st_size

    # Return the metadata as a dictionary
    return {
        'Name': os.path.basename(filepath),
        'Creation Time': creation_time,
        'Modification Time': modification_time,
        'Size': file_size
    }
filepath = 'path/to/your/dll.dll'