
import os
import shutil

def task_func(directory, backup_directory):
    # Check if the backup directory exists, if not, create it
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    # List to store the paths of copied files
    copied_files = []
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Construct full file path
            src_file_path = os.path.join(directory, filename)
            # Construct destination file path
            dst_file_path = os.path.join(backup_directory, filename)
            # Copy the file to the backup directory
            shutil.copy(src_file_path, dst_file_path)
            # Append the copied file path to the list
            copied_files.append(dst_file_path)
    
    return copied_files