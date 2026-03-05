import sys
from pathlib import Path
PATH_TO_APPEND = '/path/to/whatever'
def task_func(path_to_append=PATH_TO_APPEND):
    """
    Add a specific path to sys.path and create a directory in that path if it does not exist.
    """
    # Append the path to sys.path
    sys.path.append(path_to_append)

    # Create the directory if it does not exist
    directory = Path(path_to_append)
    if not directory.exists():
        directory.mkdir(parents=True)

    # Output the path that was appended and where the directory was created
    print(f"path_to_append: {path_to_append}")
    print(f"directory: {directory}")