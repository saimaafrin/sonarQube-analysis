import os
import shutil
def task_func(path, delimiter="/"):
    """
    Splits a given file path by a specific delimiter and computes disk usage for each directory component.
    """
    if not path or not isinstance(path, str):
        raise ValueError("Invalid path")
    if not os.path.exists(path):
        raise FileNotFoundError("Path does not exist")

    # Split the path into components
    components = path.split(delimiter)

    # Compute disk usage for each component
    usage = []
    for component in components:
        usage.append((component, shutil.disk_usage(component)))

    return usage