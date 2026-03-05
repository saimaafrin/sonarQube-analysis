import os
import errno
import shutil
def task_func(filename, dest_dir):
    """
    Copies a file to a specified destination directory and clears its contents.
    
    Parameters:
    filename (str): The path to the file to be copied.
    dest_dir (str): The destination directory path.
    
    Returns:
    str: The absolute path to the copied file within the destination directory.
    
    Raises:
    OSError: If the destination directory cannot be created and does not exist, or if the file cannot be copied.
    """
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Construct the destination file path
    dest_file = os.path.join(dest_dir, os.path.basename(filename))
    
    # Copy the file to the destination directory
    shutil.copy(filename, dest_file)
    
    # Clear the content of the original file
    with open(filename, 'w') as f:
        f.truncate(0)
    
    # Return the absolute path to the copied file
    return os.path.abspath(dest_file)