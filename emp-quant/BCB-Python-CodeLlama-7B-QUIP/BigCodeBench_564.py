
import os
import ctypes
from datetime import datetime
import pytz

def task_func(filepath):
    # Load the DLL file
    dll = ctypes.CDLL(filepath)

    # Get the metadata of the DLL file
    metadata = os.stat(filepath)

    # Convert the metadata to UTC
    creation_time = datetime.fromtimestamp(metadata.st_ctime, pytz.utc)
    modification_time = datetime.fromtimestamp(metadata.st_mtime, pytz.utc)
    size = metadata.st_size

    # Return a dictionary containing the metadata
    return {
        "Name": filepath,
        "Creation Time": creation_time,
        "Modification Time": modification_time,
        "Size": size
    }