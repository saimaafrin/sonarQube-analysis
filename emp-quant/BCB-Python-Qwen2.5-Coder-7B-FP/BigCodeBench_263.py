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
    
    # Calculate the timestamp for the specified number of days ago
    cutoff_time = now - (days_old * 24 * 60 * 60)
    
    # Search for files with specific extensions in the given directory
    for file_extension in FILE_EXTENSIONS:
        for file_path in glob.glob(os.path.join(my_path, f'*{file_extension}')):
            # Get the last modified time of the file
            file_time = os.path.getmtime(file_path)
            
            # If the file is older than the specified number of days, move it to the archive directory
            if file_time < cutoff_time:
                shutil.move(file_path, archive_path)
    
    # Return the path of the archive subdirectory
    return archive_path