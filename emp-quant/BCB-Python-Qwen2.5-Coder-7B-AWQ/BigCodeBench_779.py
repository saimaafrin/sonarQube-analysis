import os
import shutil
def get_unique_backup_dir():
    return "/fake/backup/path"
def task_func(directory):
    errors = []
    backup_dir = get_unique_backup_dir()
    try:
        # Create a backup of the directory
        shutil.copytree(directory, backup_dir)
    except Exception as e:
        errors.append(f"Error creating backup: {e}")
        return backup_dir, errors
    try:
        # Clean the original directory
        shutil.rmtree(directory)
    except Exception as e:
        errors.append(f"Error cleaning directory: {e}")
    return backup_dir, errors