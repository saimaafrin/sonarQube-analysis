
import os
import glob
import shutil
import time
# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']
def task_func(my_path: str, days_old: int) -> str:
    # Create the archive subdirectory if it doesn't exist
    archive_path = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_path):
        os.makedirs(archive_path)
    # Get the list of files in the directory
    files = glob.glob(os.path.join(my_path, '*'))
    # Iterate over the files and move the ones that are older than 'days_old'
    for file in files:
        file_name = os.path.basename(file)
        file_ext = os.path.splitext(file_name)[1]
        if file_ext in FILE_EXTENSIONS and time.time() - os.path.getmtime(file) > days_old * 86400:
            shutil.move(file, archive_path)
    return archive_path