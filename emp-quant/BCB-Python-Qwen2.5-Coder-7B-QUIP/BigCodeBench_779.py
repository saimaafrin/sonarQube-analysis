
import os
import shutil
# Constants
BACKUP_DIR = '/tmp/backup'

def get_unique_backup_dir():
    return "/fake/backup/path"

def task_func(directory):
    # Create a unique backup directory
    backup_dir = get_unique_backup_dir()
    errors = []

    try:
        # Copy the directory to the backup directory
        shutil.copytree(directory, backup_dir, dirs_exist_ok=True)
    except Exception as e:
        errors.append(f"Error during backup: {e}")

    # Clean the original directory
    try:
        shutil.rmtree(directory)
    except Exception as e:
        errors.append(f"Error during cleanup: {e}")

    return backup_dir, errors