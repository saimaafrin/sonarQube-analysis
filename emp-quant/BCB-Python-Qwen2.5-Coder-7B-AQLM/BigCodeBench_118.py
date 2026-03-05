
import os
import shutil

def task_func(directory, backup_directory):
    # Ensure the backup directory exists
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    copied_files = []
    
    # Iterate over all files in the source directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            # Construct full file path
            source_file = os.path.join(directory, filename)
            # Construct destination file path
            destination_file = os.path.join(backup_directory, filename)
            # Copy the file to the backup directory
            shutil.copy2(source_file, destination_file)
            # Append the copied file path to the list
            copied_files.append(destination_file)
    
    return copied_files