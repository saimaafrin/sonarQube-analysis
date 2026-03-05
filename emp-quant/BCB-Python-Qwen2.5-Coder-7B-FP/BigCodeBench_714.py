import sys
from pathlib import Path
PATH_TO_APPEND = '/path/to/whatever'
def task_func(path_to_append=PATH_TO_APPEND):
    """
    Appends a specific path to sys.path and creates a directory in that path if it does not exist.
    
    Args:
    path_to_append (str): The path to append and where the directory will be created. Defaults to PATH_TO_APPEND.
    
    Returns:
    str: The path that was appended and where the directory was created.
    """
    # Append the path to sys.path
    sys.path.append(path_to_append)
    
    # Create the directory if it does not exist
    path_obj = Path(path_to_append)
    if not path_obj.exists():
        path_obj.mkdir(parents=True, exist_ok=True)
    
    return path_to_append