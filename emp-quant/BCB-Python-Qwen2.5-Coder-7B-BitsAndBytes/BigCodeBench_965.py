
import os
import re
import shutil

def task_func(source_directory: str, target_directory: str, pattern: str = r"\d{4}") -> int:
    # Check if source_directory exists and is a directory
    if not os.path.exists(source_directory) or not os.path.isdir(source_directory):
        return 0
    
    # Create target_directory if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    # Initialize count of moved files
    moved_files_count = 0
    
    # Iterate over all files in the source directory
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        
        # Check if the item is a file and matches the regex pattern
        if os.path.isfile(file_path) and re.match(pattern, filename):
            try:
                # Move the file to the target directory
                shutil.move(file_path, os.path.join(target_directory, filename))
                moved_files_count += 1
            except Exception as e:
                print(f"Failed to move {filename}: {e}")
    
    return moved_files_count