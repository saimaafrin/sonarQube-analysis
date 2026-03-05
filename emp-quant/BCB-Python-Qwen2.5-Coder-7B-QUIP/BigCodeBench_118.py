
import os
import shutil

def task_func(directory, backup_directory):
    # Check if the backup directory exists, if not, create it
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # List to hold the paths of the copied files
    copied_files = []

    # Scan the specified directory for JSON files
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            # Construct the full file path
            full_path = os.path.join(directory, filename)
            # Copy the file to the backup directory
            shutil.copy(full_path, backup_directory)
            # Add the copied file path to the list
            copied_files.append(os.path.join(backup_directory, filename))

    # Return the list of copied file paths
    return copied_files