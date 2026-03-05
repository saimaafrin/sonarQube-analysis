
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
    # Construct the backup path
    backup_path = os.path.join(BACKUP_DIR, os.path.basename(directory))
    
    # Check if the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        return f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'
    
    # Check if the backup exists
    if not os.path.exists(backup_path):
        return f'Backup for directory {directory} does not exist. Cannot rollback update.'
    
    # Restore the directory from the backup
    try:
        # Remove the current directory if it exists
        if os.path.exists(directory):
            shutil.rmtree(directory)
        
        # Copy the backup to the current directory
        shutil.copytree(backup_path, directory)
        return f'Directory {directory} restored successfully from backup.'
    except Exception as e:
        return f'Failed to restore directory {directory} from backup: {str(e)}'