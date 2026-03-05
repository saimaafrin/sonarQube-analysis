
import os
import glob
import shutil

def task_func(directory, archive_dir='archive'):
    # Create the archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Get a list of all JSON files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))

    # Initialize a list to store error messages
    error_messages = []

    # Loop through each JSON file and move it to the archive directory
    for json_file in json_files:
        try:
            shutil.move(json_file, archive_dir)
        except shutil.Error as e:
            error_messages.append(f'Error moving {json_file}: {e}')

    # Return a tuple containing the boolean value and the list of error messages
    return (len(error_messages) == 0, error_messages)