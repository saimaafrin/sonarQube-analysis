import os
import shutil
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
    
    if not os.path.exists(BACKUP_DIR):
        return f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'
    
    if not os.path.exists(backup_path):
        return f'Backup for directory {directory} does not exist. Cannot rollback update.'
    
    try:
        # Remove the current directory
        if os.path.exists(directory):
            shutil.rmtree(directory)
        
        # Restore the directory from the backup
        shutil.copytree(backup_path, directory)
        return directory
    except Exception as e:
        return f'Error during rollback: {str(e)}'