import os
import shutil
BACKUP_DIR = '/tmp/backup'
def task_func(directory):
    """
    Rollback the update of a directory by restoring it from a backup.
    
    Parameters:
    - directory (str): The directory path to rollback.
    
    Returns:
    - directory (str): The restored directory path if successful, otherwise an error message.
    
    Requirements:
    - os
    - shutil
    
    Constants:
    - BACKUP_DIR: The directory where backups are stored. Default is '/tmp/backup'.
    
    Examples:
    >>> task_func('/tmp/my_data')
    '/tmp/my_data'
    
    >>> task_func('/tmp/nonexistent')
    'Backup directory /tmp/backup does not exist. Cannot rollback update.'
    
    Note: 
    - This function will return the restored directory path on successful rollback, or an error message otherwise.
    """
    if not os.path.exists(BACKUP_DIR):
        return 'Backup directory ' + BACKUP_DIR + ' does not exist. Cannot rollback update.'
    if not os.path.exists(directory):
        return 'Directory ' + directory + ' does not exist. Cannot rollback update.'
    if not os.path.exists(directory + '.bak'):
        return 'Backup file ' + directory + '.bak does not exist. Cannot rollback update.'
    shutil.copy(directory + '.bak', directory)
    return directory