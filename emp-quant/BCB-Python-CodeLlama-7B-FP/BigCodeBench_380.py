import re
import os
import shutil
def task_func(directory):
    """
    Arrange files in a directory by their extensions.
    Create a new directory for each extension and move the files to the corresponding directories.
    """
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Iterate over the files and group them by extension
    for file in files:
        # Get the extension of the file
        extension = os.path.splitext(file)[1]

        # Create a new directory for the extension if it doesn't exist
        if not os.path.exists(f"{directory}/{extension}"):
            os.mkdir(f"{directory}/{extension}")

        # Move the file to the corresponding directory
        shutil.move(f"{directory}/{file}", f"{directory}/{extension}/{file}")
directory = "path/to/directory"