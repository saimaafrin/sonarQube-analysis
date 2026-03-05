
import shutil
import pathlib
from typing import List

def task_func(source_path, destination_path):
    # Check if the source path exists and is a directory
    source_dir = pathlib.Path(source_path)
    if not source_dir.exists() or not source_dir.is_dir():
        raise ValueError("Source path does not exist or is not a directory")
    
    # Ensure the destination directory exists
    destination_dir = pathlib.Path(destination_path)
    destination_dir.mkdir(parents=True, exist_ok=True)
    
    # List all files in the source directory
    files_copied = []
    for file in source_dir.iterdir():
        if file.is_file():
            # Copy the file to the destination directory
            shutil.copy(file, destination_dir)
            files_copied.append(file.name)
    
    # Return the source directory name and the list of copied files
    return source_dir.name, files_copied