import re
import os
import shutil
def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Initialize the count of moved files
    moved_files_count = 0
    
    # Compile the regular expression pattern for better performance
    pattern = re.compile(file_pattern)
    
    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file name matches the pattern
        if pattern.match(filename):
            # Construct full file path
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)
            
            # Move the file to the target directory
            shutil.move(source_file, target_file)
            moved_files_count += 1
    
    return moved_files_count