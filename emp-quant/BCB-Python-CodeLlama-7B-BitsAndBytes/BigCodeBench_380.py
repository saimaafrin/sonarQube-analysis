
import re
import os
import shutil

def task_func(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Create a dictionary to store the files grouped by extension
    file_dict = {}

    # Iterate over the files and group them by extension
    for file in files:
        # Get the extension of the file
        extension = os.path.splitext(file)[1]

        # Add the file to the dictionary using the extension as the key
        if extension not in file_dict:
            file_dict[extension] = []
        file_dict[extension].append(file)

    # Create a new directory for each extension and move the files to it
    for extension, files in file_dict.items():
        # Create a new directory with the extension as the name
        new_dir = os.path.join(directory, extension)
        os.mkdir(new_dir)

        # Move the files to the new directory
        for file in files:
            shutil.move(os.path.join(directory, file), new_dir)

    # Output the result
    print(None)