
import os
import shutil

def task_func(src_dir, dest_dir, extension):
    # Initialize the count of files moved
    files_moved = 0
    
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Iterate over all files in the source directory
    for filename in os.listdir(src_dir):
        # Check if the file has the specified extension
        if filename.endswith(extension):
            # Construct full file path
            src_file_path = os.path.join(src_dir, filename)
            dest_file_path = os.path.join(dest_dir, filename)
            
            # Move the file to the destination directory
            shutil.move(src_file_path, dest_file_path)
            files_moved += 1
    
    return files_moved