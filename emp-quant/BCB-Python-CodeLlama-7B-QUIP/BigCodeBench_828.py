
import os
import errno
import shutil

def task_func(filename, dest_dir):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Copy the file to the destination directory
        shutil.copy(filename, dest_dir)

        # Clear the contents of the original file
        with open(filename, 'w') as f:
            f.write('')

        return dest_dir
    except (OSError, IOError) as e:
        raise e