
import os
import glob
import shutil
import time

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:
    """
    Archive files that were changed older than a specified number of days in a given directory.

    Args:
        my_path (str): The path of the directory to search for files.
        days_old (int): The number of days old the files must be to be archived.

    Returns:
        str: The path of the archive subdirectory where files are moved.
    """
    # Create the archive subdirectory if it doesn't exist
    archive_path = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_path):
        os.makedirs(archive_path)

    # Get a list of files in the directory that are older than 'days_old'
    files_to_archive = []
    for ext in FILE_EXTENSIONS:
        files_to_archive.extend(glob.glob(os.path.join(my_path, '*' + ext)))
    files_to_archive = [f for f in files_to_archive if os.path.getmtime(f) < time.time() - days_old * 86400]

    # Move the files to the archive subdirectory
    for file in files_to_archive:
        shutil.move(file, archive_path)

    return archive_path