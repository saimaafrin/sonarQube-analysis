
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
        # Create backup directory
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        # Copy all files and directories from the source to the backup directory
        for item in os.listdir(directory):
            source_item = os.path.join(directory, item)
            backup_item = os.path.join(backup_dir, item)
            if os.path.isdir(source_item):
                shutil.copytree(source_item, backup_item)
            else:
                shutil.copy2(source_item, backup_item)
        
        # Clean the original directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
            except Exception as e:
                errors.append(f"Error cleaning {item_path}: {e}")
        
        return backup_dir, errors
    except Exception as e:
        errors.append(f"Error during backup and cleanup: {e}")
        return backup_dir, errors