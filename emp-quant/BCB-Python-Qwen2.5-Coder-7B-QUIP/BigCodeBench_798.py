
import os
import shutil
# Constants
BACKUP_DIR = '/tmp/backup'

def task_func(directory):
    """
    Rollback the update of a directory by restoring it from a backup.
    
    Args:
    directory (str): The directory to rollback.
    
    Returns:
    str: The restored directory path if successful, otherwise an error message.
    """
    backup_path = os.path.join(BACKUP_DIR, directory)
    if not os.path.exists(backup_path):
        return f'Backup directory {backup_path} does not exist. Cannot rollback update.'
    
    # Remove the current directory
    if os.path.exists(directory):
        shutil.rmtree(directory)
    
    # Restore from backup
    shutil.copytree(backup_path, directory)
    
    return directory