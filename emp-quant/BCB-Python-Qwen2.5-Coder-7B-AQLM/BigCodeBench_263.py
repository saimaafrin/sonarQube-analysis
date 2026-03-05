
import os
import glob
import shutil
import time

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:
    # Create the archive directory if it doesn't exist
    archive_path = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_path):
        os.makedirs(archive_path)
    
    # Get the current time
    now = time.time()
    # Calculate the cutoff time
    cutoff = now - (days_old * 24 * 60 * 60)
    
    # Search for files with specific extensions in the given directory
    for file_path in glob.glob(os.path.join(my_path, '*')):
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] in FILE_EXTENSIONS:
            # Get the last modified time of the file
            file_mtime = os.path.getmtime(file_path)
            # If the file is older than the cutoff time, move it to the archive directory
            if file_mtime < cutoff:
                shutil.move(file_path, archive_path)
    
    return archive_path