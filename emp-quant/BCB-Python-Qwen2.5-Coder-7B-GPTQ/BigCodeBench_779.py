import os
import shutil
import tempfile
BACKUP_DIR = '/tmp/backup'
def get_unique_backup_dir():
    return tempfile.mkdtemp(dir=BACKUP_DIR)
def task_func(directory):
    errors = []
    backup_dir = get_unique_backup_dir()
    
    try:
        # Create backup of the directory
        shutil.copytree(directory, backup_dir)
    except Exception as e:
        errors.append(f"Error creating backup: {e}")
        return backup_dir, errors
    
    # Clean the original directory
    try:
        shutil.rmtree(directory)
    except Exception as e:
        errors.append(f"Error cleaning directory: {e}")
    
    return backup_dir, errors