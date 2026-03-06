
import os
import glob
import shutil
import time

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:
    # Create the archive subdirectory if it doesn't exist
    archive_dir = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Get a list of files in the directory that are older than 'days_old'
    files_to_archive = []
    for ext in FILE_EXTENSIONS:
        files_to_archive.extend(glob.glob(os.path.join(my_path, '*' + ext)))
    files_to_archive = [f for f in files_to_archive if os.path.getmtime(f) < time.time() - (days_old * 24 * 60 * 60)]

    # Move the files to the archive subdirectory
    for file in files_to_archive:
        shutil.move(file, archive_dir)

    return archive_dir