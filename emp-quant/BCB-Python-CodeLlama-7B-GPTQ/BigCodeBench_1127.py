import os
import re
import hashlib
def task_func(path, delimiter):
    """
    Splits a file path by a specified delimiter, retaining the delimiter in the output, and computes the hash of each component if it is a file.
    The function should output with:
        list[tuple]: A list of tuples, where each tuple contains a path component and its hash (if it's a file).
        If the component is not a file, its hash will be None.
    """
    # Split the path by the delimiter
    path_components = path.split(delimiter)

    # Compute the hash of each component if it is a file
    hashes = []
    for component in path_components:
        if os.path.isfile(component):
            hashes.append((component, hashlib.md5(component).hexdigest()))
        else:
            hashes.append((component, None))

    return hashes
path = "path/to/file.txt"
delimiter = "/"