import os
import glob
import shutil
def task_func(directory, archive_dir='archive'):
    """
    Archive all JSON files in a given directory by moving them to a specified archive directory.
    The function should output with:
        tuple: A tuple containing a boolean value and a list of error messages.
        The boolean is True if all files are successfully moved, and False otherwise.
        The list contains error messages for each file that failed to move.
    """
    # Check if the directory exists
    if not os.path.isdir(directory):
        return (False, [f"Directory {directory} does not exist"])

    # Check if the archive directory exists
    if not os.path.isdir(archive_dir):
        return (False, [f"Archive directory {archive_dir} does not exist"])

    # Get a list of all JSON files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))

    # Move each JSON file to the archive directory
    for json_file in json_files:
        try:
            shutil.move(json_file, archive_dir)
        except Exception as e:
            return (False, [f"Error moving {json_file}: {e}"])

    return (True, [])
directory = 'path/to/directory'
archive_dir = 'path/to/archive/directory'