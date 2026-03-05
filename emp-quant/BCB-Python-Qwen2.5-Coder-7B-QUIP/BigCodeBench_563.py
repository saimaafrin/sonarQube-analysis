
import ctypes
import os
import shutil
import glob

def task_func(filepath, destination_dir):
    # Load the DLL file
    dll_name = os.path.basename(filepath)
    dll_path = os.path.abspath(filepath)
    ctypes.CDLL(dll_path)
    
    # Get the directory of the DLL file
    dll_directory = os.path.dirname(dll_path)
    
    # Move all DLL files in the same directory to the destination directory
    for dll_file in glob.glob(os.path.join(dll_directory, '*.dll')):
        shutil.move(dll_file, destination_dir)
    
    # Return the name of the loaded DLL file
    return dll_name