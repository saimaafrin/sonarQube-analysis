
import os
import shutil

def task_func(directory, backup_directory):
    # Create the backup directory if it does not exist
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # Get a list of JSON files in the source directory
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

    # Copy the JSON files to the backup directory
    copied_files = []
    for json_file in json_files:
        src_path = os.path.join(directory, json_file)
        dst_path = os.path.join(backup_directory, json_file)
        shutil.copy(src_path, dst_path)
        copied_files.append(dst_path)

    return copied_files