
import pathlib
import os

def task_func(path: str, delimiter: str = os.path.sep) -> list:
    # Validate the path
    if not pathlib.Path(path).isfile():
        raise ValueError("Invalid path")

    # Split the path into components
    components = path.split(delimiter)

    # Remove empty components
    components = [component for component in components if component != ""]

    return components