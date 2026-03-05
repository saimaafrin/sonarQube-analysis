import os
import glob
import shutil
def task_func(directory, archive_dir='archive'):
    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Find all JSON files in the given directory
    json_files = glob.glob(os.path.join(directory, '*.json'))

    # List to hold error messages
    error_messages = []

    # Move each JSON file to the archive directory
    for json_file in json_files:
        try:
            # Construct the destination path
            destination = os.path.join(archive_dir, os.path.basename(json_file))
            # Move the file
            shutil.move(json_file, destination)
        except Exception as e:
            # Append error message if the file could not be moved
            error_messages.append(f"Failed to move {json_file}: {str(e)}")

    # Determine if all files were moved successfully
    success = len(error_messages) == 0

    # Return the result as a tuple
    return success, error_messages