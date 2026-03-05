import os
import shutil
def task_func(directory, backup_directory):
    # Check if the backup directory exists, if not, create it
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    # List to store paths of copied files
    copied_files = []
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Construct full file path
            file_path = os.path.join(directory, filename)
            # Construct backup file path
            backup_file_path = os.path.join(backup_directory, filename)
            # Copy the file to the backup directory
            shutil.copy(file_path, backup_file_path)
            # Add the copied file path to the list
            copied_files.append(backup_file_path)
    
    # Return the list of copied file paths
    return copied_files