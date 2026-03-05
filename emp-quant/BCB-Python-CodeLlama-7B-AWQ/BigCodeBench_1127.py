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

    # Create a list to store the tuples
    result = []

    # Iterate over the path components
    for component in path_components:
        # If the component is a file, compute its hash
        if os.path.isfile(component):
            with open(component, 'rb') as f:
                hash = hashlib.sha256(f.read()).hexdigest()
        else:
            hash = None

        # Add the tuple to the result list
        result.append((component, hash))

    return result
path = '/path/to/file.txt'
delimiter = '/'