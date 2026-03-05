
import os
import errno
import shutil

def task_func(filename, dest_dir):
    # Check if the destination directory exists, if not, create it
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    # Construct the full path to the destination file
    dest_file = os.path.join(dest_dir, os.path.basename(filename))

    # Copy the file to the destination directory
    try:
        shutil.copy2(filename, dest_file)
    except OSError as e:
        raise

    # Clear the content of the original file
    with open(filename, 'w') as file:
        file.truncate(0)

    # Return the absolute path to the copied file
    return os.path.abspath(dest_file)