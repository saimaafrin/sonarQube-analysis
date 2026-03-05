import shutil
import pathlib
from typing import List, Tuple
def task_func(source_path: str, destination_path: str) -> Tuple[str, List[str]]:
    # Convert paths to Path objects for easier manipulation
    source_dir = pathlib.Path(source_path)
    destination_dir = pathlib.Path(destination_path)
    
    # Check if source_path exists and is a directory
    if not source_dir.exists() or not source_dir.is_dir():
        raise ValueError("source_path does not exist or is not a directory")
    
    # Ensure the destination directory exists
    destination_dir.mkdir(parents=True, exist_ok=True)
    
    # List to hold the names of the copied files
    copied_files = []
    
    # Iterate over the files in the source directory
    for item in source_dir.iterdir():
        if item.is_file():
            # Construct the full path of the file in the destination directory
            destination_file = destination_dir / item.name
            # Copy the file to the destination directory
            shutil.copy(item, destination_file)
            # Append the filename to the list
            copied_files.append(item.name)
    
    # Return the source directory name and the list of copied files
    return source_dir.name, copied_files