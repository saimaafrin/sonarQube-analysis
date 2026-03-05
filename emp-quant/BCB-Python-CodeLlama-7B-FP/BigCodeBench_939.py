import re
import os
import glob
def task_func(dir_path: str) -> list:
    """
    Rename all files in the specified directory by removing all special characters, punctuation marks, and spaces, using regular expressions.
    The function keeps alphanumeric characters and removes the rest.
    The function should output with:
        list[str]: A list containing the new names of all files after renaming.
    """
    # Get a list of all files in the directory
    files = glob.glob(os.path.join(dir_path, '*'))

    # Create a list to store the new file names
    new_files = []

    # Iterate over the files and rename them
    for file in files:
        # Get the file name and extension
        filename, file_extension = os.path.splitext(file)

        # Remove special characters, punctuation marks, and spaces from the file name
        new_filename = re.sub(r'[^a-zA-Z0-9]', '', filename)

        # Add the new file name to the list
        new_files.append(new_filename + file_extension)

    return new_files
dir_path = 'path/to/directory'