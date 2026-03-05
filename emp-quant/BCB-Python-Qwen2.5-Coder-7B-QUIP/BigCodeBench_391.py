
import os
import glob
import shutil

def task_func(directory, archive_dir='archive'):
    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))

    # Initialize a list to store error messages
    error_messages = []

    # Move each JSON file to the archive directory
    for json_file in json_files:
        try:
            shutil.move(json_file, os.path.join(archive_dir, os.path.basename(json_file)))
        except Exception as e:
            error_messages.append(f"Failed to move {json_file}: {str(e)}")

    # Check if all files were moved successfully
    all_files_moved = len(error_messages) == 0

    # Return a tuple with the result and error messages
    return all_files_moved, error_messages