import shutil
import pathlib
from typing import List, Tuple
def task_func(source_path: str, destination_path: str) -> Tuple[str, List[str]]:
    source_dir = pathlib.Path(source_path)
    destination_dir = pathlib.Path(destination_path)

    # Check if source_path exists and is a directory
    if not source_dir.exists() or not source_dir.is_dir():
        raise ValueError("source_path does not exist or is not a directory")

    # List to store the names of the files copied
    copied_files = []

    # Iterate over the files in the source directory
    for item in source_dir.iterdir():
        if item.is_file():
            # Construct the destination file path
            destination_file = destination_dir / item.name
            # Copy the file to the destination directory
            shutil.copy(item, destination_file)
            # Append the file name to the copied_files list
            copied_files.append(item.name)

    # Return the source directory name and the list of copied files
    return source_dir.name, copied_files