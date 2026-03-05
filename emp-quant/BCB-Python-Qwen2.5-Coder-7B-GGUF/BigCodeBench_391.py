
import os
import glob
import shutil

def task_func(directory, archive_dir='archive'):
    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # List all JSON files in the given directory
    json_files = glob.glob(os.path.join(directory, '*.json'))

    # Initialize a list to store error messages
    error_messages = []

    # Move each JSON file to the archive directory
    for file_path in json_files:
        try:
            # Construct the destination path
            destination_path = os.path.join(archive_dir, os.path.basename(file_path))
            # Move the file
            shutil.move(file_path, destination_path)
        except Exception as e:
            # Append error message if the file move fails
            error_messages.append(f"Failed to move {file_path}: {str(e)}")

    # Determine if all files were moved successfully
    success = len(error_messages) == 0

    # Return the result as a tuple
    return success, error_messages