
import re
import os
import glob

def task_func(dir_path: str) -> list:
    """
    Rename all files in the specified directory by removing all special characters, punctuation marks, and spaces, using regular expressions.
    The function keeps alphanumeric characters and removes the rest.
    """
    file_names = os.listdir(dir_path)
    new_file_names = []
    for file_name in file_names:
        new_file_name = re.sub(r'[^a-zA-Z0-9\.]', '', file_name)
        new_file_names.append(new_file_name)
    return new_file_names