
import os
import glob
from collections import Counter

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    """
    Traverses a given directory recursively to count files by specified extensions.

    Args:
        directory (str): The directory to traverse.
        extensions (list of str): The extensions to count.
        keep_zero (bool): Whether to keep counts for extensions with zero files.

    Returns:
        Counter: An object containing counts of files for each of the specified extensions.

    Raises:
        OSError: If the specified directory does not exist.
    """
    if not os.path.exists(directory):
        raise OSError("Directory does not exist: {}".format(directory))

    # Create a list to store the counts for each extension
    counts = [0] * len(extensions)

    # Traverse the directory recursively and count files for each extension
    for root, dirs, files in os.walk(directory):
        for file in files:
            for i, ext in enumerate(extensions):
                if file.endswith(ext):
                    counts[i] += 1

    # Create a Counter object from the counts
    counter = Counter(counts)

    # Filter out counts for extensions with zero files if keep_zero is False
    if not keep_zero:
        counter = counter.filter(lambda x: x[1] > 0)

    return counter