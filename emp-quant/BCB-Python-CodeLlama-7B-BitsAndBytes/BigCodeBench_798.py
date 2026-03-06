
import os
import shutil

# Constants
BACKUP_DIR = '/tmp/backup'

def task_func(directory):
    if not os.path.exists(BACKUP_DIR):
        return 'Backup directory {} does not exist. Cannot rollback update.'.format(BACKUP_DIR)

    backup_file = os.path.join(BACKUP_DIR, directory)
    if not os.path.exists(backup_file):
        return 'Backup file {} does not exist. Cannot rollback update.'.format(backup_file)

    try:
        shutil.copy(backup_file, directory)
        return directory
    except Exception as e:
        return 'Error restoring backup: {}'.format(e)

print(task_func('/tmp/nonexistent'))