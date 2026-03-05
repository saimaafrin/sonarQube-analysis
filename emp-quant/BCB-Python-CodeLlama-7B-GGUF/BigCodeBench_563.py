
import ctypes
import os
import shutil
import glob

def task_func(filepath, destination_dir):
    # Load the DLL file
    dll_handle = ctypes.CDLL(filepath)

    # Get the name of the loaded DLL file
    dll_name = os.path.basename(filepath)

    # Move all DLL files in the same directory to the destination directory
    for file in glob.glob(os.path.join(os.path.dirname(filepath), "*.dll")):
        shutil.move(file, destination_dir)

    return dll_name