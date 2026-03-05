import re
import os
import shutil
def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    """
    Moves files from the source directory to the target directory based on a specified pattern.
    
    Parameters:
    - source_dir (str): The path to the source directory.
    - target_dir (str): The path to the target directory.
    - file_pattern (str): The regex pattern to match file names.
    
    Returns:
    - moved_files_count (int): The number of files that were successfully moved.
    """
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Initialize the count of moved files
    moved_files_count = 0
    
    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file name matches the specified pattern
        if re.match(file_pattern, filename):
            # Construct full file paths
            source_file_path = os.path.join(source_dir, filename)
            target_file_path = os.path.join(target_dir, filename)
            
            # Move the file to the target directory
            shutil.move(source_file_path, target_file_path)
            moved_files_count += 1
    
    return moved_files_count