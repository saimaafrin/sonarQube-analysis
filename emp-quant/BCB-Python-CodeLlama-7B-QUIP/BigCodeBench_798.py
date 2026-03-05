
import os
import shutil
# Constants
BACKUP_DIR = '/tmp/backup'
def task_func(directory):
    try:
        # Check if the backup directory exists
        if not os.path.exists(BACKUP_DIR):
            raise ValueError('Backup directory ' + BACKUP_DIR + ' does not exist. Cannot rollback update.')
        # Restore the directory from the backup
        shutil.copytree(BACKUP_DIR, directory)
        return directory
    except ValueError as e:
        return e