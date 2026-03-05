
import os
import shutil

def task_func(src_folder, backup_dir):
    try:
        # Backup the source folder to the specified backup directory
        shutil.copytree(src_folder, backup_dir)
        # Delete the source folder
        os.rmdir(src_folder)
        return True
    except ValueError:
        raise ValueError("Source folder does not exist")
    except OSError:
        raise OSError("Error while deleting source folder")
    return False