
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
    
    # Initialize the count of moved files
    moved_files_count = 0
    
    # Iterate over all files in the source directory
    for filename in os.listdir(source_directory):
        # Construct the full file path
        file_path = os.path.join(source_directory, filename)
        
        # Check if the file is a regular file and matches the pattern
        if os.path.isfile(file_path) and re.match(pattern, filename):
            # Construct the destination file path
            destination_path = os.path.join(target_directory, filename)
            
            # Move the file to the target directory
            shutil.move(file_path, destination_path)
            
            # Increment the count of moved files
            moved_files_count += 1
    
    # Return the number of files successfully moved
    return moved_files_count