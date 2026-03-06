import os
import glob
import shutil
import time
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']
def task_func(my_path: str, days_old: int) -> str:
    """
    Archive files that were changed older than a specified number of days in a given directory. This function searches for files with specific extensions (.txt, .csv, .xlsx, .docx, .pdf) in the given directory.
    Files older than 'days_old' are moved to an 'archive' subdirectory within the specified directory.

    Parameters:
    my_path (str): The path of the directory to search.
    days_old (int): The age of files to archive, in days.

    Returns:
    str: The path of the archive subdirectory where files are moved.

    Requirements:
    - os
    - glob
    - shutil
    - time

    Example:
    >>> task_func('/usr/my_directory', 30)
    '/usr/my_directory/archive'
    """
    # Get the current time
    current_time = time.time()

    # Get the path of the archive subdirectory
    archive_path = os.path.join(my_path, 'archive')

    # Create the archive subdirectory if it doesn't exist
    if not os.path.exists(archive_path):
        os.mkdir(archive_path)

    # Get the list of files in the directory
    file_list = glob.glob(os.path.join(my_path, '*'))

    # Iterate through the list of files
    for file in file_list:
        # Get the file's last modified time
        last_modified = os.path.getmtime(file)

        # If the file is older than 'days_old' days, move it to the archive subdirectory
        if current_time - last_modified > days_old * 86400:
            # Get the file's extension
            file_extension = os.path.splitext(file)[1]

            # If the file's extension is in FILE_EXTENSIONS, move it to the archive subdirectory
            if file_extension in FILE_EXTENSIONS:
                shutil.move(file, archive_path)

    # Return the path of the archive subdirectory
    return archive_path