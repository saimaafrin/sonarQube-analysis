
import sys
from pathlib import Path

# Constants
PATH_TO_APPEND = '/path/to/whatever'

def task_func(path_to_append=PATH_TO_APPEND):
    # Add the specified path to sys.path
    sys.path.append(path_to_append)
    
    # Create the directory if it does not exist
    path_obj = Path(path_to_append)
    if not path_obj.exists():
        path_obj.mkdir(parents=True, exist_ok=True)
    
    return path_to_append