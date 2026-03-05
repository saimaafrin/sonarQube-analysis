import ctypes
import os
import shutil
import glob
def task_func(filepath, destination_dir):
    """
    Loads a DLL file specified by the given filepath and moves all DLL files in the same directory to another specified directory.
    This function demonstrates file operations including DLL loading, file path manipulation, and file moving using ctypes, os, shutil, and glob modules.
    """
    # Load the DLL file
    dll_path = os.path.abspath(filepath)
    dll_handle = ctypes.CDLL(dll_path)

    # Get the DLL file name
    dll_name = os.path.basename(dll_path)

    # Move all DLL files in the same directory to the destination directory
    dll_dir = os.path.dirname(dll_path)
    for file in glob.glob(os.path.join(dll_dir, "*.dll")):
        shutil.move(file, destination_dir)

    # Return the name of the loaded DLL file
    return dll_name
filepath = "path/to/my/dll.dll"
destination_dir = "path/to/destination/dir"