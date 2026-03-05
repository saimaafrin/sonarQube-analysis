import os
import glob
import shutil
import time
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']
def task_func(my_path: str, days_old: int) -> str:
    """
    Archive files that were changed older than a specified number of days in a given directory.
    This function searches for files with specific extensions (.txt, .csv, .xlsx, .docx, .pdf) in the given directory.
    Files older than 'days_old' are moved to an 'archive' subdirectory within the specified directory.
    """
    # Create the archive subdirectory if it does not exist
    archive_dir = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Get the list of files in the directory
    files = glob.glob(os.path.join(my_path, '*'))

    # Iterate over the files and move them to the archive subdirectory
    for file in files:
        # Check if the file is an archive file
        if os.path.splitext(file)[1] in FILE_EXTENSIONS:
            # Get the file modification time
            mod_time = os.path.getmtime(file)

            # Check if the file is older than the specified number of days
            if time.time() - mod_time > days_old * 86400:
                # Move the file to the archive subdirectory
                shutil.move(file, archive_dir)

    # Return the path of the archive subdirectory
    return archive_dir
my_path = '/path/to/directory'
days_old = 30