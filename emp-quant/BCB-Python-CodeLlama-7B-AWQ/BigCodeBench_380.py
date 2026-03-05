import re
import os
import shutil
def task_func(directory):
    """
    Arrange files in a directory by their extensions. Create a new directory for each extension and move the files to the corresponding directories.
    """
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Create a dictionary to store the files and their extensions
    file_dict = {}

    # Iterate over the files and extract their extensions
    for file in files:
        extension = os.path.splitext(file)[1]
        if extension not in file_dict:
            file_dict[extension] = []
        file_dict[extension].append(file)

    # Create a new directory for each extension
    for extension, files in file_dict.items():
        new_dir = os.path.join(directory, extension)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        # Move the files to the corresponding directories
        for file in files:
            shutil.move(os.path.join(directory, file), new_dir)

    return None
directory = "path/to/directory"