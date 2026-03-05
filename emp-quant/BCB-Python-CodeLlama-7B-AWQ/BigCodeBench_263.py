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
    # Create the archive directory if it does not exist
    archive_dir = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Get the list of files in the directory
    files = glob.glob(os.path.join(my_path, '*'))

    # Iterate over the files and move them to the archive directory if they are older than 'days_old'
    for file in files:
        if os.path.isfile(file) and os.path.splitext(file)[1] in FILE_EXTENSIONS:
            file_age = time.time() - os.path.getmtime(file)
            if file_age > days_old * 86400:
                shutil.move(file, archive_dir)

    return archive_dir
my_path = '/path/to/directory'
days_old = 30