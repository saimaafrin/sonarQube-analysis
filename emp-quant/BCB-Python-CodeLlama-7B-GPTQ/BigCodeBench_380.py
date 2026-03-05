import re
import os
import shutil
def task_func(directory):
    """
    Arrange files in a directory by their extensions. Create a new directory for each extension and move the files to the corresponding directories.
    """
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Create a dictionary to store the files by extension
    files_by_ext = {}

    # Iterate over the files and add them to the dictionary
    for file in files:
        # Get the extension of the file
        ext = os.path.splitext(file)[1]

        # Add the file to the dictionary
        if ext in files_by_ext:
            files_by_ext[ext].append(file)
        else:
            files_by_ext[ext] = [file]

    # Iterate over the dictionary and create a new directory for each extension
    for ext, files in files_by_ext.items():
        # Create a new directory for the extension
        new_dir = os.path.join(directory, ext)
        os.mkdir(new_dir)

        # Move the files to the new directory
        for file in files:
            src = os.path.join(directory, file)
            dst = os.path.join(new_dir, file)
            shutil.move(src, dst)

    # Output
    print(None)
directory = "path/to/directory"