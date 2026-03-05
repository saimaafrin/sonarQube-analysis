import os
import shutil
import tempfile
BACKUP_DIR = '/tmp/backup'
def get_unique_backup_dir():
    return tempfile.mkdtemp(dir=BACKUP_DIR)
def task_func(directory):
    errors = []
    try:
        # Create a unique backup directory
        backup_dir = get_unique_backup_dir()
        
        # Copy the contents of the directory to the backup directory
        for item in os.listdir(directory):
            s = os.path.join(directory, item)
            d = os.path.join(backup_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        
        # Clean the original directory
        for item in os.listdir(directory):
            s = os.path.join(directory, item)
            try:
                if os.path.isdir(s):
                    shutil.rmtree(s)
                else:
                    os.remove(s)
            except Exception as e:
                errors.append(f"Error cleaning {s}: {e}")
        
        return backup_dir, errors
    except Exception as e:
        errors.append(f"Error during backup and cleanup: {e}")
        return None, errors