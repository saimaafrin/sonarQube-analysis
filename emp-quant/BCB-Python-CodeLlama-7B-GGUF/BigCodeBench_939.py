
import re
import os
import glob

def task_func(dir_path: str) -> list:
    """
    Rename all files in the specified directory by removing all special characters, punctuation marks, and spaces, using regular expressions.
    The function keeps alphanumeric characters and removes the rest.
    """
    file_list = glob.glob(os.path.join(dir_path, '*'))
    new_file_list = []
    for file in file_list:
        new_name = re.sub(r'[^a-zA-Z0-9\.]', '', file)
        new_file_list.append(new_name)
    return new_file_list