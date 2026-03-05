import os
import shutil
BACKUP_DIR = '/tmp/backup'
def task_func(directory):
    # Check if the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        return 'Backup directory {} does not exist. Cannot rollback update.'.format(BACKUP_DIR)
    # Check if the directory exists
    if not os.path.exists(directory):
        return 'Directory {} does not exist. Cannot rollback update.'.format(directory)
    # Check if the directory is a directory
    if not os.path.isdir(directory):
        return 'Directory {} is not a directory. Cannot rollback update.'.format(directory)
    # Check if the directory is not the backup directory
    if directory == BACKUP_DIR:
        return 'Cannot rollback update of the backup directory.'.format(directory)
    # Restore the directory from the backup
    shutil.copytree(os.path.join(BACKUP_DIR, directory), directory)
    return directory