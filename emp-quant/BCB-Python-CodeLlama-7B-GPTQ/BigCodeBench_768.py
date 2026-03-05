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

    # Create a dictionary to store the results
    results = {}

    # Iterate over all text files in the directory and its subdirectories
    for file in glob.iglob(os.path.join(dir_path, "**", "*.txt"), recursive=True):
        # Open the file and read its contents
        with open(file, "r") as f:
            contents = f.read()

        # Count the occurrences of the word "error" in the file
        count = len(re.findall(r"\berror\b", contents, re.IGNORECASE))

        # Add the result to the dictionary
        results[os.path.relpath(file, dir_path)] = count

    return results
dir_path = "path/to/directory"