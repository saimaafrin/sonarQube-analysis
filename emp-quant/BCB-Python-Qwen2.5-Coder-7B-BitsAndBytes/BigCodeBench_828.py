
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

    # Construct the full destination path
    dest_path = os.path.join(dest_dir, os.path.basename(filename))

    # Copy the file to the destination directory
    try:
        shutil.copy2(filename, dest_path)
    except IOError as e:
        raise OSError(f"Failed to copy file: {e}")

    # Clear the content of the original file
    open(filename, 'w').close()

    return os.path.abspath(dest_path)