
import ctypes
import os
import shutil
import glob

def task_func(filepath, destination_dir):
    # Load the DLL file
    dll_name = os.path.basename(filepath)
    try:
        ctypes.cdll.LoadLibrary(filepath)
        print(f"Successfully loaded {dll_name}")
    except Exception as e:
        return f"Failed to load {dll_name}: {e}"

    # Move all DLL files in the same directory to the destination directory
    source_dir = os.path.dirname(filepath)
    dll_files = glob.glob(os.path.join(source_dir, '*.dll'))
    
    for dll_file in dll_files:
        if dll_file != filepath:
            shutil.move(dll_file, destination_dir)
            print(f"Moved {dll_file} to {destination_dir}")

    return dll_name