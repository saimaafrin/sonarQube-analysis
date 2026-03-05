import os
import shutil
BACKUP_DIR = '/tmp/backup'
def task_func(directory):
    if not os.path.exists(BACKUP_DIR):
        return 'Backup directory {} does not exist. Cannot rollback update.'.format(BACKUP_DIR)
    if not os.path.exists(directory):
        return 'Directory {} does not exist. Cannot rollback update.'.format(directory)
    if not os.path.isdir(directory):
        return 'Directory {} is not a directory. Cannot rollback update.'.format(directory)
    if not os.path.exists(os.path.join(BACKUP_DIR, directory)):
        return 'Backup directory {} does not exist. Cannot rollback update.'.format(os.path.join(BACKUP_DIR, directory))
    if not os.path.isdir(os.path.join(BACKUP_DIR, directory)):
        return 'Backup directory {} is not a directory. Cannot rollback update.'.format(os.path.join(BACKUP_DIR, directory))
    try:
        shutil.copytree(os.path.join(BACKUP_DIR, directory), directory)
        return directory
    except Exception as e:
        return 'Error restoring directory {}: {}'.format(directory, e)