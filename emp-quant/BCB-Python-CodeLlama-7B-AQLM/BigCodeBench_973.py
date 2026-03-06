import os
import shutil
def task_func(path, delimiter="/"):
    """
    Splits a given file path by a specific delimiter and computes disk usage for each directory component.

    Parameters:
    - path (str): The file path to split.
    - delimiter (str, optional): The delimiter to use for splitting the path. Default is '/'.

    Returns:
    list: A list of tuples where each tuple contains a path component and its disk usage as a dictionary.
          The disk usage dictionary contains keys 'total', 'used', and 'free'.

    Raises:
    - ValueError: If the 'path' is empty, not a string, or contain invalid components.
    - FileNotFoundError: If the 'path' does not exist in the filesystem.

    Requirements:
    - os
    - shutil

    Examples:
    >>> task_func('Docs/src', '/')
    [('Docs', {'total': 100, 'used': 50, 'free': 50}), ('src', {'total': 200, 'used': 100, 'free': 100})]

    >>> task_func('a/b', '/')
    [('a', {'total': 300, 'used': 150, 'free': 150}), ('b', {'total': 400, 'used': 200, 'free': 200})]
    """
    if not path or not isinstance(path, str):
        raise ValueError("The 'path' must be a non-empty string.")

    if not os.path.exists(path):
        raise FileNotFoundError("The 'path' does not exist in the filesystem.")

    if not os.path.isfile(path):
        raise ValueError("The 'path' must be a file.")

    path_components = path.split(delimiter)
    if len(path_components) == 1:
        raise ValueError("The 'path' must contain at least one component.")

    if path_components[0] == "":
        raise ValueError("The 'path' must not start with a delimiter.")

    if path_components[-1] == "":
        raise ValueError("The 'path' must not end with a delimiter.")

    for component in path_components:
        if not component or component == delimiter:
            raise ValueError("The 'path' must not contain empty components.")

    result = []
    current_path = ""
    for component in path_components:
        current_path += component + delimiter
        disk_usage = shutil.disk_usage(current_path)
        result.append((component, {"total": disk_usage.total, "used": disk_usage.used, "free": disk_usage.free}))

    return result