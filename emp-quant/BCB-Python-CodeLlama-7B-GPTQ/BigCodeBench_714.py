import sys
from pathlib import Path
PATH_TO_APPEND = '/path/to/whatever'
def task_func(path_to_append=PATH_TO_APPEND):
    """
    Add a specific path to sys.path and create a directory in that path if it does not exist.
    """
    # Check if the path exists
    if not Path(path_to_append).exists():
        # Create the directory
        Path(path_to_append).mkdir(parents=True, exist_ok=True)

    # Append the path to sys.path
    sys.path.append(path_to_append)

    # Output the path that was appended and where the directory was created
    print(f"path_to_append: {path_to_append}")