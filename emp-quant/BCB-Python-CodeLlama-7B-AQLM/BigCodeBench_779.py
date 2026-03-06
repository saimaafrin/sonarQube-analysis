import os
import shutil
def get_unique_backup_dir():
    return "/fake/backup/path"
def task_func(directory):
    """
    Create a backup of a directory and clean the directory afterwards.
    
    Parameters:
    - directory (str): The directory path to be backed up and cleaned.
    
    Returns:
    tuple: A tuple containing:
        - str: The backup directory path.
        - list: A list of any errors encountered during the operation (empty list if no errors).
    
    Requirements:
    - os
    - shutil
    - time
    
    Example:
    >>> task_func('/tmp/my_data')
    ('/tmp/backup/backup_20230827010101', [])
    
    Note: The function will return the backup directory path and a list of errors (if any).
    """
    # Create a backup directory
    backup_dir = get_unique_backup_dir()
    # Create a backup of the directory
    shutil.copytree(directory, backup_dir)
    # Clean the directory
    shutil.rmtree(directory)
    # Return the backup directory path and a list of errors (if any)
    return backup_dir, []