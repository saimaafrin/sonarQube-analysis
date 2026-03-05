
import os
import glob
import shutil
import time
# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:
    # Define the archive directory path
    archive_dir = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Get the current time
    now = time.time()

    # Search for files with specific extensions
    for ext in FILE_EXTENSIONS:
        search_pattern = os.path.join(my_path, f'*{ext}')
        for file_path in glob.glob(search_pattern):
            # Check if the file is older than 'days_old'
            if os.path.getmtime(file_path) < now - days_old * 86400:
                # Move the file to the archive directory
                shutil.move(file_path, archive_dir)
                print(f"Moved {file_path} to {archive_dir}")

    return archive_dir