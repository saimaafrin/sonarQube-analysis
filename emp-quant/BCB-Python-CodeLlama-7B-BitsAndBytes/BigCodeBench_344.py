
import os
import shutil

def task_func(src_folder, backup_dir):
    """
    Backs up a given source folder to the specified backup directory, then deletes the source folder.

    Parameters:
        src_folder (str): The source folder to back up and delete.
        backup_dir (str): The backup directory to store the backed up files.

    Returns:
        bool: True if the operation is successful, False otherwise.

    Raises:
        ValueError: If the source folder does not exist.
        Exception: If an error occurs while deleting the source folder.
    """
    if not os.path.exists(src_folder):
        raise ValueError(f"Source folder {src_folder} does not exist.")

    try:
        shutil.copytree(src_folder, backup_dir)
        shutil.rmtree(src_folder)
        return True
    except Exception as e:
        print(f"Error occurred while deleting source folder {src_folder}: {e}")
        return False