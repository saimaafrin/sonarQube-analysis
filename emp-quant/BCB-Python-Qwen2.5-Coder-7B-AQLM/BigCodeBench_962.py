
import os
from pathlib import Path
import glob
import shutil

def task_func(source_directory: str, target_directory: str) -> int:
    # Check if the source directory exists
    if not Path(source_directory).exists():
        raise FileNotFoundError(f"The source directory {source_directory} does not exist.")
    
    # Define the extensions to filter
    extensions = {".txt", ".docx", ".xlsx", ".csv"}
    
    # Initialize the count of moved files
    moved_files_count = 0
    
    # Walk through the source directory recursively
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            # Check if the file has one of the specified extensions
            if Path(file).suffix in extensions:
                # Construct the full path of the source file
                source_file_path = Path(root) / file
                
                # Construct the target file path
                target_file_path = Path(target_directory) / file
                
                # Handle naming conflicts by renaming duplicates
                if target_file_path.exists():
                    base_name, extension = target_file_path.stem, target_file_path.suffix
                    n = 1
                    while True:
                        new_target_file_path = Path(target_directory) / f"{base_name}-{n}{extension}"
                        if not new_target_file_path.exists():
                            target_file_path = new_target_file_path
                            break
                        n += 1
                
                # Move the file to the target directory
                shutil.move(source_file_path, target_file_path)
                moved_files_count += 1
    
    return moved_files_count