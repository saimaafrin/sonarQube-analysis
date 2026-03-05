
import os
import shutil
import tempfile

# Constants
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
    
    try:
        # Clean the original directory
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    except Exception as e:
        errors.append(f"Error cleaning directory: {e}")
    
    return backup_dir, errors