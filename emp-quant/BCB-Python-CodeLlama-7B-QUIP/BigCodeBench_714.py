
import sys
from pathlib import Path

# Constants
PATH_TO_APPEND = '/path/to/whatever'

def task_func(path_to_append=PATH_TO_APPEND):
    # Check if the path exists
    if not Path(path_to_append).exists():
        # Create the directory if it does not exist
        Path(path_to_append).mkdir(exist_ok=True)

    # Append the path to sys.path
    sys.path.append(path_to_append)

    return path_to_append

# Call the function
path_to_append = task_func()

# Print the path
print(path_to_append)