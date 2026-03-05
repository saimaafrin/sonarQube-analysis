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
        # Get the file name without the extension
        file_name = os.path.splitext(file)[0]

        # Remove all special characters, punctuation marks, and spaces
        new_file_name = re.sub(r'[^a-zA-Z0-9]', '', file_name)

        # Add the new file name to the list
        new_files.append(new_file_name)

    # Return the list of new file names
    return new_files
dir_path = 'path/to/directory'