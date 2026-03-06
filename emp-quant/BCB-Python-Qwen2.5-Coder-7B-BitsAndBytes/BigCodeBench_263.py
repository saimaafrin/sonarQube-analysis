
import os
import glob
import shutil
import time

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:
    # Create the archive directory if it doesn't exist
    archive_dir = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Get the current time and calculate the cutoff time
    now = time.time()
    cutoff_time = now - (days_old * 86400)  # 86400 seconds in a day
    
    # Find all files with the specified extensions
    files_to_archive = []
    for ext in FILE_EXTENSIONS:
        files_to_archive.extend(glob.glob(os.path.join(my_path, f'*{ext}')))
    
    # Move files older than cutoff_time to the archive directory
    for file_path in files_to_archive:
        if os.path.getmtime(file_path) < cutoff_time:
            shutil.move(file_path, archive_dir)
    
    return archive_dir