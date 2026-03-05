import shutil
import pathlib
from typing import List
def task_func(source_path, destination_path):
    # Check if the source path exists and is a directory
    source_dir = pathlib.Path(source_path)
    if not source_dir.exists() or not source_dir.is_dir():
        raise ValueError("Source path does not exist or is not a directory")
    
    # List files in the source directory
    files_to_copy = [f.name for f in source_dir.iterdir() if f.is_file()]
    
    # Create the destination directory if it does not exist
    destination_dir = pathlib.Path(destination_path)
    destination_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy files to the destination directory
    for file_name in files_to_copy:
        shutil.copy2(source_dir / file_name, destination_dir)
    
    # Return the name of the source directory and the list of copied files
    return (source_dir.name, files_to_copy)