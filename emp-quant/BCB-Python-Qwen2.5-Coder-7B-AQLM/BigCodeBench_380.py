
import re
import os
import shutil

def task_func(directory):
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        # Construct full file path
        file_path = os.path.join(directory, filename)
        # Check if it is a file and not a directory
        if os.path.isfile(file_path):
            # Extract the file extension
            extension = os.path.splitext(filename)[1]
            # Create a directory for the extension if it doesn't exist
            extension_dir = os.path.join(directory, extension[1:])
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)
            # Move the file to the corresponding extension directory
            shutil.move(file_path, os.path.join(extension_dir, filename))
    return None