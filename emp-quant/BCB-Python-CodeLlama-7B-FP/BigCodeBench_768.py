import re
import os
import glob
def task_func(dir_path):
    """
    Search for occurrences of the word "error" in all text files within a specified directory and its subdirectories.
    The function specifically searches for the word "error" in text files (with the extension ".txt").
    This function is NOT case sensitive, e.g. also "ERROr" will be counted.
    The function should raise the exception for: ValueError: If directory in dir_path does not exist.
    The function should output with:
        dict: A dictionary with relative file paths as keys and the count of
        occurrences of the word "error" as values.
    """
    if not os.path.exists(dir_path):
        raise ValueError("Directory does not exist")

    file_paths = glob.glob(os.path.join(dir_path, "**", "*.txt"), recursive=True)
    error_counts = {}
    for file_path in file_paths:
        with open(file_path, "r") as file:
            text = file.read()
            error_counts[file_path] = len(re.findall(r"\berror\b", text, re.IGNORECASE))

    return error_counts