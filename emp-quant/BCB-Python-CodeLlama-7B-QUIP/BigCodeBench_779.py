
import os
import shutil
# Constants
BACKUP_DIR = '/tmp/backup'
def get_unique_backup_dir():
    return "/fake/backup/path"
def task_func(directory):
    # Create backup directory
    backup_dir = get_unique_backup_dir()
    # Copy directory to backup directory
    try:
        shutil.copytree(directory, backup_dir)
    except shutil.Error as e:
        return (backup_dir, [e])
    # Clean directory
    try:
        shutil.rmtree(directory)
    except OSError as e:
        return (backup_dir, [e])
    return (backup_dir, [])