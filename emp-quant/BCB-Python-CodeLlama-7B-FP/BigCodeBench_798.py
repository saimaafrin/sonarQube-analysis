import os
import shutil
BACKUP_DIR = '/tmp/backup'
def task_func(directory):
    # Check if the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        return 'Backup directory {} does not exist. Cannot rollback update.'.format(BACKUP_DIR)
    # Check if the directory to be rolled back exists
    if not os.path.exists(directory):
        return 'Directory {} does not exist. Cannot rollback update.'.format(directory)
    # Get the latest backup
    latest_backup = max(os.listdir(BACKUP_DIR))
    # Restore the directory from the latest backup
    shutil.copytree(os.path.join(BACKUP_DIR, latest_backup), directory)
    return directory