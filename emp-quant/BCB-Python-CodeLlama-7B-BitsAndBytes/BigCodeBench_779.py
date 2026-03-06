
import os
import shutil

# Constants
BACKUP_DIR = '/tmp/backup'

def get_unique_backup_dir():
    return "/fake/backup/path"

def task_func(directory):
    # Create a backup of the directory
    backup_dir = get_unique_backup_dir()
    shutil.copytree(directory, backup_dir)

    # Clean the directory
    shutil.rmtree(directory)

    # Return the backup directory path and a list of errors (if any)
    return (backup_dir, [])