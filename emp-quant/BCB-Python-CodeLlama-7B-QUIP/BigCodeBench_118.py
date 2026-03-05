
import os
import shutil

def task_func(directory, backup_directory):
    # Check if the backup directory exists
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # Get a list of JSON files in the source directory
    json_files = [f for f in os.listdir(directory) if os.path.splitext(f)[1] == '.json']

    # Copy the JSON files to the backup directory
    for json_file in json_files:
        shutil.copy(os.path.join(directory, json_file), backup_directory)

    # Return the list of copied files
    return [os.path.join(backup_directory, json_file) for json_file in json_files]