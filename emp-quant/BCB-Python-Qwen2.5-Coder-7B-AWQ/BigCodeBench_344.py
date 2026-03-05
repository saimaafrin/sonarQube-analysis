import os
import shutil
def task_func(src_folder, backup_dir):
    try:
        # Check if the source folder exists
        if not os.path.exists(src_folder):
            raise ValueError("Source folder does not exist.")
        
        # Backup the source folder to the specified backup directory
        shutil.copytree(src_folder, backup_dir)
        
        # Delete the source folder
        shutil.rmtree(src_folder)
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False