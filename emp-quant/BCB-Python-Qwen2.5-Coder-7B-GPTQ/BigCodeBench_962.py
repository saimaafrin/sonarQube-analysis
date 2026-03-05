import os
from pathlib import Path
import glob
import shutil
def task_func(source_directory: str, target_directory: str) -> int:
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"The source directory {source_directory} does not exist.")
    
    # Define the file extensions to filter
    extensions = ['.txt', '.docx', '.xlsx', '.csv']
    
    # Initialize a counter for the number of files moved
    files_moved = 0
    
    # Walk through the source directory recursively
    for root, _, files in os.walk(source_directory):
        for file in files:
            # Check if the file has one of the specified extensions
            if Path(file).suffix in extensions:
                # Construct the full path of the source file
                source_file_path = os.path.join(root, file)
                
                # Construct the target file path
                target_file_path = os.path.join(target_directory, file)
                
                # Check if the target file already exists
                if os.path.exists(target_file_path):
                    # Generate a new filename by appending a number
                    base, ext = os.path.splitext(file)
                    n = 1
                    while os.path.exists(target_file_path):
                        new_file = f"{base}-{n}{ext}"
                        target_file_path = os.path.join(target_directory, new_file)
                        n += 1
                
                # Move the file to the target directory
                shutil.move(source_file_path, target_file_path)
                files_moved += 1
    
    return files_moved