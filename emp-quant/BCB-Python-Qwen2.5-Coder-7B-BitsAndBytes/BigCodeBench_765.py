
import os
from pathlib import Path
import shutil

def task_func(kwargs, target_dir="non_none_files"):
    """
    Processes files from a dictionary by checking if the file exists,
    and if it has content, then copies it to a target directory.

    Args:
        kwargs (dict): A dictionary containing file paths as keys and their contents as values.
        target_dir (str): The target directory where files will be copied. Defaults to "non_none_files".

    Returns:
        copied_files (list): A list of full file paths that were copied.
    """
    # Ensure the target directory exists
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)

    copied_files = []

    for file_path, content in kwargs.items():
        source_path = Path(file_path)
        
        # Check if the file exists
        if not source_path.exists():
            print(f"File {file_path} does not exist.")
            continue
        
        # Check if the file has content
        if not content.strip():
            print(f"File {file_path} is empty.")
            continue
        
        # Construct the destination path
        dest_path = target_path / source_path.name
        
        # Copy the file to the target directory
        shutil.copy2(source_path, dest_path)
        copied_files.append(str(dest_path))

    return copied_files