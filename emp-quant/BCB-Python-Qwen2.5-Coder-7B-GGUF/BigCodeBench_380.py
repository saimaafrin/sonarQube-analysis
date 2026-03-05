
import re
import os
import shutil

def task_func(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is not a directory
        if os.path.isfile(os.path.join(directory, filename)):
            # Extract the file extension
            _, ext = os.path.splitext(filename)
            # Create a new directory for the extension if it doesn't exist
            ext_dir = os.path.join(directory, ext[1:])  # Remove the leading dot
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            # Move the file to the corresponding extension directory
            shutil.move(os.path.join(directory, filename), os.path.join(ext_dir, filename))
    return None