import os
import glob
import shutil
def task_func(directory, archive_dir='archive'):
    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Find all JSON files in the given directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    
    # Initialize a list to store error messages
    error_messages = []
    
    # Attempt to move each JSON file to the archive directory
    for file_path in json_files:
        try:
            # Construct the destination path
            dest_path = os.path.join(archive_dir, os.path.basename(file_path))
            # Move the file
            shutil.move(file_path, dest_path)
        except Exception as e:
            # If an error occurs, add it to the error messages list
            error_messages.append(f"Failed to move {file_path}: {str(e)}")
    
    # Determine if all files were moved successfully
    success = len(error_messages) == 0
    
    # Return a tuple with the success status and error messages
    return success, error_messages