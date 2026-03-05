
import os
import shutil

def task_func(src_folder, backup_dir):
    # Check if the source folder exists
    if not os.path.exists(src_folder):
        raise ValueError("Source folder does not exist")
    
    # Backup the source folder to the backup directory
    backup_path = os.path.join(backup_dir, os.path.basename(src_folder))
    shutil.copytree(src_folder, backup_path)
    
    # Delete the source folder
    try:
        shutil.rmtree(src_folder)
        return True
    except Exception as e:
        print(f"Error deleting source folder: {e}")
        return False