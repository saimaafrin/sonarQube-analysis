import os
import glob
import shutil
import time
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']
def task_func(my_path: str, days_old: int) -> str:
    # Create the archive directory if it doesn't exist
    archive_path = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_path):
        os.makedirs(archive_path)
    
    # Get the current time and calculate the cutoff time
    current_time = time.time()
    cutoff_time = current_time - (days_old * 24 * 60 * 60)
    
    # Find all files with the specified extensions
    files_to_archive = []
    for ext in FILE_EXTENSIONS:
        files_to_archive.extend(glob.glob(os.path.join(my_path, f'*{ext}')))
    
    # Move files older than 'days_old' to the archive directory
    for file_path in files_to_archive:
        if os.path.getmtime(file_path) < cutoff_time:
            shutil.move(file_path, archive_path)
    
    return archive_path