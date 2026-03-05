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
    
    # Get the current time
    now = time.time()
    
    # Calculate the timestamp for the files older than 'days_old'
    cutoff_time = now - (days_old * 24 * 60 * 60)
    
    # Find all files with the specified extensions in the given directory
    for file_path in glob.glob(os.path.join(my_path, '*')):
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] in FILE_EXTENSIONS:
            # Get the file's last modified time
            file_mtime = os.path.getmtime(file_path)
            # If the file is older than 'days_old', move it to the archive directory
            if file_mtime < cutoff_time:
                shutil.move(file_path, archive_path)
    
    # Return the path of the archive subdirectory
    return archive_path