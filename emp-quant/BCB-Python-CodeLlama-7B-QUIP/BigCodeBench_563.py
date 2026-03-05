
import ctypes
import os
import shutil
import glob

def task_func(filepath, destination_dir):
    # Load the DLL file
    dll = ctypes.CDLL(filepath)

    # Get the directory of the DLL file
    dll_dir = os.path.dirname(filepath)

    # Move all DLL files in the same directory to the destination directory
    for file in glob.glob(dll_dir + "/*.dll"):
        shutil.move(file, destination_dir)

    # Return the name of the loaded DLL file
    return os.path.basename(filepath)