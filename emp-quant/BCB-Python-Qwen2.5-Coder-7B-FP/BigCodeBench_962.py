import os
from pathlib import Path
import glob
import shutil
def task_func(source_directory: str, target_directory: str) -> int:
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"The source directory {source_directory} does not exist.")
    
    # Define the extensions to filter
    extensions = {".txt", ".docx", ".xlsx", ".csv"}
    
    # Initialize the count of moved files
    moved_files_count = 0
    
    # Walk through the source directory recursively
    for root, _, files in os.walk(source_directory):
        for file in files:
            # Check if the file has one of the specified extensions
            if Path(file).suffix in extensions:
                # Construct the full path of the source file
                source_file_path = os.path.join(root, file)
                
                # Construct the target file path
                target_file_path = os.path.join(target_directory, file)
                
                # Handle naming conflicts by renaming duplicates
                if os.path.exists(target_file_path):
                    base, ext = os.path.splitext(file)
                    n = 1
                    while os.path.exists(target_file_path):
                        target_file_path = os.path.join(target_directory, f"{base}-{n}{ext}")
                        n += 1
                
                # Move the file to the target directory
                shutil.move(source_file_path, target_file_path)
                moved_files_count += 1
    
    return moved_files_count