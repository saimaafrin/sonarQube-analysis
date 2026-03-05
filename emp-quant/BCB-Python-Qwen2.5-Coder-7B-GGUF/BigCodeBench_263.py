
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
    
    # Calculate the timestamp for files older than 'days_old'
    cutoff_time = time.time() - (days_old * 24 * 60 * 60)
    
    # Search for files with specific extensions in the given directory
    for file_extension in FILE_EXTENSIONS:
        for file_path in glob.glob(os.path.join(my_path, f'*{file_extension}')):
            # Check if the file is older than 'days_old'
            if os.path.getmtime(file_path) < cutoff_time:
                # Move the file to the archive directory
                shutil.move(file_path, archive_path)
    
    return archive_path