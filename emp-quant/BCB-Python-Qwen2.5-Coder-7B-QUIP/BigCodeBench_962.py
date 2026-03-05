
import os
from pathlib import Path
import glob
import shutil

def task_func(source_directory: str, target_directory: str):
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist.")

    # Define the extensions to filter by
    extensions = ['.txt', '.docx', '.xlsx', '.csv']

    # Initialize a counter for the number of files moved
    files_moved = 0

    # Recursively scan the source directory for files with the specified extensions
    for ext in extensions:
        for file_path in glob.glob(f"{source_directory}/**/*{ext}", recursive=True):
            # Get the base name and extension of the file
            base_name, ext = os.path.splitext(file_path)
            base_name = os.path.basename(base_name)

            # Construct the target file path
            target_file_path = os.path.join(target_directory, base_name + ext)

            # Check if the target file already exists and rename if necessary
            if os.path.exists(target_file_path):
                n = 1
                while os.path.exists(target_file_path):
                    target_file_path = os.path.join(target_directory, f"{base_name}-{n}{ext}")
                    n += 1

            # Move the file to the target directory
            shutil.move(file_path, target_file_path)
            files_moved += 1

    return files_moved