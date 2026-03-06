import os
import re
import hashlib
def task_func(path, delimiter):
    """
    Splits a file path by a specified delimiter, retaining the delimiter in the output, and computes the hash of each component if it is a file.
    
    Parameters:
    path (str): The file path to split.
    delimiter (str): The delimiter to use for splitting the path.

    Returns:
    list[tuple]: A list of tuples, where each tuple contains a path component and its hash (if it's a file).
                 If the component is not a file, its hash will be None.

    Requirements:
    - os
    - re
    - hashlib

    Example:
    >>> task_func("Docs/src/file.txt", "/")
    [('Docs', None), ('/', None), ('src', None), ('/', None), ('file.txt', 'hash_value')]
    """
    path_list = path.split(delimiter)
    hash_list = []
    for path_component in path_list:
        if os.path.isfile(path_component):
            hash_list.append((path_component, hashlib.md5(open(path_component, 'rb').read()).hexdigest()))
        else:
            hash_list.append((path_component, None))
    return hash_list