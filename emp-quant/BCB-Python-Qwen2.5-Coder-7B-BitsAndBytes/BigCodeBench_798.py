
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
    # Construct the backup path for the given directory
    backup_path = os.path.join(BACKUP_DIR, directory)

    # Check if the backup directory exists
    if not os.path.exists(backup_path):
        return f'Backup directory {backup_path} does not exist. Cannot rollback update.'

    # Restore the directory from the backup
    try:
        # Remove the current directory if it exists
        if os.path.exists(directory):
            shutil.rmtree(directory)
        
        # Copy the backup directory to the original directory
        shutil.copytree(backup_path, directory)
        return directory
    except Exception as e:
        return f'Failed to restore directory: {e}'