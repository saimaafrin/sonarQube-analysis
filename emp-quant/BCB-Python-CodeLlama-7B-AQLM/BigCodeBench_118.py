import os
import shutil
def task_func(directory, backup_directory):
    """
    Scans a specified directory for JSON files and copies them to a backup directory.
    If the backup directory does not exist, it is created.
    The function returns a list of paths to the copied files in the backup directory.

    Parameters:
    - directory (str): The path of the directory to scan for JSON files.
    - backup_directory (str): The path of the directory where JSON files will be backed up.

    Returns:
    - list: Paths to the copied JSON files in the backup directory.

    Note: The function assumes that the source directory exists and contains JSON files.

    Requirements:
    - os
    - shutil

    Examples:
    >>> directory = 'path/to/source'
    >>> backup_directory = 'path/to/backup'
    >>> type(task_func(directory, backup_directory)) is list
    True
    >>> all(file.endswith('.json') for file in task_func(directory, backup_directory))
    True
    """
    if not os.path.exists(backup_directory):
        os.mkdir(backup_directory)
    files = os.listdir(directory)
    copied_files = []
    for file in files:
        if file.endswith('.json'):
            shutil.copy(os.path.join(directory, file), os.path.join(backup_directory, file))
            copied_files.append(os.path.join(backup_directory, file))
    return copied_files