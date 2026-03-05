
import ctypes
import os
import shutil
import glob

def task_func(filepath, destination_dir):
    # Load the DLL file
    dll_name = os.path.basename(filepath)
    dll = ctypes.CDLL(filepath)
    
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Move all DLL files in the same directory to the destination directory
    current_dir = os.path.dirname(filepath)
    dll_files = glob.glob(os.path.join(current_dir, '*.dll'))
    for dll_file in dll_files:
        if dll_file != filepath:
            shutil.move(dll_file, destination_dir)
    
    # Return the name of the loaded DLL file
    return dll_name