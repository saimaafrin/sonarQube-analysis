
import os
import shutil

# Constants
BACKUP_DIR = '/tmp/backup'

def get_unique_backup_dir():
    # This is a placeholder for generating a unique backup directory path
    # In a real scenario, you would use a more robust method to ensure uniqueness
    return "/fake/backup/path"

def task_func(directory):
    """
    Creates a backup of the specified directory and then cleans it.
    
    Args:
    directory (str): The path to the directory to be backed up and cleaned.
    
    Returns:
    tuple: A tuple containing:
        str: The backup directory path.
        list: A list of any errors encountered during the operation (empty list if no errors).
    """
    errors = []
    backup_directory = get_unique_backup_dir()
    
    try:
        # Create the backup directory
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)
        
        # Copy all files from the original directory to the backup directory
        for item in os.listdir(directory):
            s = os.path.join(directory, item)
            d = os.path.join(backup_directory, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        
        # Clean the original directory
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        
        # Remove the original directory itself
        os.rmdir(directory)
        
    except Exception as e:
        errors.append(str(e))
    
    return backup_directory, errors