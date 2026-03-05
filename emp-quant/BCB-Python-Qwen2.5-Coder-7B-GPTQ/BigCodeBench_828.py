import os
import errno
import shutil
def task_func(filename, dest_dir):
    # Check if the destination directory exists, if not, create it
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Construct the full path for the destination file
    dest_file = os.path.join(dest_dir, os.path.basename(filename))
    
    # Copy the file to the destination directory
    shutil.copy(filename, dest_file)
    
    # Clear the content of the original file
    open(filename, 'w').close()
    
    # Return the absolute path to the copied file
    return os.path.abspath(dest_file)