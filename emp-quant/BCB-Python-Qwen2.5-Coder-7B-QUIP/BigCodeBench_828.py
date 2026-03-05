
import os
import errno
import shutil

def task_func(filename, dest_dir):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    # Copy the file to the destination directory
    dest_file = os.path.join(dest_dir, os.path.basename(filename))
    shutil.copy(filename, dest_file)

    # Clear the content of the original file
    open(filename, 'w').close()

    # Return the absolute path to the copied file
    return os.path.abspath(dest_file)