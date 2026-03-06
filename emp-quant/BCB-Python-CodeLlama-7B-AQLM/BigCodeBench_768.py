import re
import os
import glob
def task_func(dir_path):
    """
    Search for occurrences of the word "error" in all text files within a 
    specified directory and its subdirectories.
    
    Parameters:
    dir_path (str): The path of the directory.
    
    Returns:
    dict: A dictionary with relative file paths as keys and the count of 
            occurrences of the word "error" as values.
    
    Raises:
    - ValueError: If directory in dir_path does not exist.

    Requirements:
    - re: For regex pattern matching.
    - os: For retrieving relative file paths.
    - glob: For fetching all text file paths in the directory.
    
    The function specifically searches for the word "error" in text files
    (with the extension ".txt").
    This function is NOT case sensitive, e.g. also "ERROr" will be counted.
    
    Example:
    >>> task_func("/path/to/directory")
    {'file1.txt': 2, 'subdir/file2.txt': 1}
    """
    if not os.path.exists(dir_path):
        raise ValueError("Directory does not exist.")
    file_paths = glob.glob(dir_path + "**/*.txt", recursive=True)
    file_dict = {}
    for file_path in file_paths:
        with open(file_path, "r") as file:
            file_text = file.read()
            file_dict[os.path.relpath(file_path, dir_path)] = len(re.findall(r"\berror\b", file_text, re.IGNORECASE))
    return file_dict