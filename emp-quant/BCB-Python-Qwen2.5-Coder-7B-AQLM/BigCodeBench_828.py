
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

    # Construct the destination file path
    dest_file_path = os.path.join(dest_dir, os.path.basename(filename))

    # Copy the file to the destination directory
    try:
        shutil.copy2(filename, dest_file_path)
    except OSError as e:
        raise

    # Clear the content of the original file
    with open(filename, 'w') as file:
        file.truncate(0)

    # Return the absolute path to the copied file
    return os.path.abspath(dest_file_path)