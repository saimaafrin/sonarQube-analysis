import re
import os
import glob
def task_func(dir_path: str) -> list:
    """
    Rename all files in the specified directory by removing all special characters,
    punctuation marks, and spaces, using regular expressions. The function keeps
    alphanumeric characters and removes the rest.

    Requirements:
    - re
    - os
    - glob

    Parameters:
    dir_path (str): The path to the directory containing the files to be renamed.

    Returns:
    list[str]: A list containing the new names of all files after renaming.

    Example:
    >>> task_func('path/to/directory')
    ['file1', 'file2', 'file3']
    >>> task_func('another/directory/path')
    ['anotherFile1', 'anotherFile2']
    """
    # Get all files in the directory
    files = glob.glob(os.path.join(dir_path, '*'))

    # Create a list to store the new names of the files
    new_names = []

    # Iterate through all files
    for file in files:
        # Get the name of the file
        name = os.path.basename(file)

        # Remove all special characters, punctuation marks, and spaces
        new_name = re.sub(r'[^a-zA-Z0-9]+', '', name)

        # Add the new name to the list
        new_names.append(new_name)

        # Rename the file
        os.rename(file, os.path.join(dir_path, new_name))

    # Return the new names of the files
    return new_names