
import re
import os
import shutil

def task_func(directory):
    # Create a dictionary to store the files by extension
    files_by_ext = {}

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Get the file's extension
        ext = os.path.splitext(file)[1]

        # Add the file to the dictionary using the extension as the key
        if ext not in files_by_ext:
            files_by_ext[ext] = []
        files_by_ext[ext].append(file)

    # Create a new directory for each extension
    for ext, files in files_by_ext.items():
        # Create a new directory with the extension as the name
        new_dir = os.path.join(directory, ext)
        os.mkdir(new_dir)

        # Move the files to the new directory
        for file in files:
            shutil.move(os.path.join(directory, file), new_dir)

    # Output None
    print(None)

# Call the function with the directory path
task_func("path/to/directory")