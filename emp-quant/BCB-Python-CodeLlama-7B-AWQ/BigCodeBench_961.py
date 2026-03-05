import os
import glob
from collections import Counter
def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    """
    Traverses a given directory recursively to count files by specified extensions.
    Note that: This function counts files in a case-sensitive manner.
    The function should raise the exception for: OSError: If the specified directory does not exist.
    The function should output with:
        Counter: An object containing counts of files for each of the specified extensions.
    """
    if not os.path.exists(directory):
        raise OSError("The specified directory does not exist.")

    # Create a list of all files in the directory and its subdirectories
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))

    # Filter the list of files to only include files with the specified extensions
    files_with_extensions = [file for file in all_files if file.endswith(extensions)]

    # Count the number of files for each extension
    counts = Counter()
    for file in files_with_extensions:
        extension = os.path.splitext(file)[1]
        counts[extension] += 1

    # Return the counts
    return counts
directory = "path/to/directory"
extensions = [".txt", ".docx", ".xlsx", ".csv"]
keep_zero = True