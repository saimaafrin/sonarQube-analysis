import ctypes
import os
import shutil
import glob
def task_func(filepath, destination_dir):
    # Load the DLL file specified by the given filepath
    dll_file = ctypes.CDLL(filepath)

    # Get the directory path of the DLL file
    dll_dir = os.path.dirname(filepath)

    # Move all DLL files in the same directory to the destination directory
    for file in glob.glob(os.path.join(dll_dir, "*.dll")):
        shutil.move(file, destination_dir)

    # Output the name of the loaded DLL file
    return os.path.basename(filepath)
filepath = "path/to/my/dll.dll"
destination_dir = "path/to/destination/dir"