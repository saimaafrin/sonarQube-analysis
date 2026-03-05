import re
import os
import glob
def task_func(dir_path):
    """
    Search for occurrences of the word "error" in all text files within a specified directory and its subdirectories.
    The function specifically searches for the word "error" in text files (with the extension ".txt").
    This function is NOT case sensitive, e.g. also "ERROr" will be counted.
    The function should raise the exception for:
        ValueError: If directory in dir_path does not exist.
    The function should output with:
        dict: A dictionary with relative file paths as keys and the count of
        occurrences of the word "error" as values.
    """
    if not os.path.exists(dir_path):
        raise ValueError("Directory does not exist")

    # Create a dictionary to store the results
    results = {}

    # Iterate over all files in the directory and its subdirectories
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Check if the file is a text file with the extension ".txt"
            if file.endswith(".txt"):
                # Open the file and read its contents
                with open(os.path.join(root, file), "r") as f:
                    contents = f.read()

                # Use regular expressions to count the occurrences of the word "error"
                pattern = re.compile(r"\berror\b", re.IGNORECASE)
                matches = pattern.findall(contents)

                # Add the number of occurrences to the results dictionary
                results[file] = len(matches)

    return results
dir_path = "path/to/directory"