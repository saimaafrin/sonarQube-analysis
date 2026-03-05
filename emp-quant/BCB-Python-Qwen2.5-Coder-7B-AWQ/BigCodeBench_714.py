import sys
from pathlib import Path
PATH_TO_APPEND = '/path/to/whatever'
def task_func(path_to_append=PATH_TO_APPEND):
    """
    Adds a specific path to sys.path and creates a directory in that path if it does not exist.

    Args:
    path_to_append (str): The path to append and where the directory will be created. Defaults to PATH_TO_APPEND.

    Returns:
    str: The path that was appended and where the directory was created.
    """
    # Add the path to sys.path
    sys.path.append(path_to_append)
    
    # Create a Path object for the given path
    path_obj = Path(path_to_append)
    
    # Check if the directory exists, if not, create it
    if not path_obj.exists():
        path_obj.mkdir(parents=True, exist_ok=True)
    
    return path_to_append