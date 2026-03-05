
import sys
from pathlib import Path
# Constants
PATH_TO_APPEND = '/path/to/whatever'

def task_func(path_to_append=PATH_TO_APPEND):
    # Append the path to sys.path
    sys.path.append(path_to_append)
    
    # Create the directory if it does not exist
    path = Path(path_to_append)
    if not path.exists():
        path.mkdir()
    
    # Return the path that was appended
    return path_to_append