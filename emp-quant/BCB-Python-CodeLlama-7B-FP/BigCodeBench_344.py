import os
import shutil
def task_func(src_folder, backup_dir):
    """
    Backs up a given source folder to the specified backup directory, then deletes the source folder.
    The function should raise the exception for:
        ValueError: If the source folder does not exist.
        Exception: If an error occurs while deleting the source folder.
    The function should output with:
        bool: True if the operation is successful, False otherwise.
    """
    if not os.path.exists(src_folder):
        raise ValueError(f"Source folder {src_folder} does not exist.")

    try:
        shutil.copytree(src_folder, backup_dir)
        shutil.rmtree(src_folder)
    except Exception as e:
        raise Exception(f"Error occurred while deleting source folder {src_folder}: {e}")

    return True
src_folder = "test_folder"
backup_dir = "backup_folder"