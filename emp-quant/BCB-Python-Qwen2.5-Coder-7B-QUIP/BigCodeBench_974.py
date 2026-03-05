
import shutil
import pathlib
from typing import List, Tuple

def task_func(source_path, destination_path):
    # Convert the source and destination paths to Path objects
    source_path = pathlib.Path(source_path)
    destination_path = pathlib.Path(destination_path)

    # Check if the source path exists and is a directory
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError("Source path does not exist or is not a directory")

    # Get the list of files in the source directory
    files = [f for f in source_path.iterdir() if f.is_file()]

    # Copy each file to the destination directory
    copied_files = []
    for file in files:
        shutil.copy(file, destination_path)
        copied_files.append(file.name)

    # Return the name of the source directory and the list of copied files
    return (source_path.name, copied_files)