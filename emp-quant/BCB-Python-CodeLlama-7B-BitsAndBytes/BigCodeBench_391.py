
import os
import glob
import shutil

def task_func(directory, archive_dir='archive'):
    """
    Archive all JSON files in a given directory by moving them to a specified archive directory.

    Parameters:
    directory (str): The directory containing the JSON files to be archived.
    archive_dir (str): The directory where the JSON files will be moved to.

    Returns:
    tuple: A tuple containing a boolean value and a list of error messages.
        The boolean is True if all files are successfully moved, and False otherwise.
        The list contains error messages for each file that failed to move.
    """
    # Get a list of all JSON files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))

    # Create the archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Move each JSON file to the archive directory
    for file in json_files:
        try:
            shutil.move(file, os.path.join(archive_dir, os.path.basename(file)))
        except Exception as e:
            return False, [f'Error moving file {file}: {e}']

    return True, []