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

    components = path.split(delimiter)
    disk_usage = []
    for component in components:
        if not os.path.exists(component):
            raise FileNotFoundError("Component does not exist")
        du = shutil.disk_usage(component)
        disk_usage.append((component, du))

    return disk_usage
path = "a/b"
delimiter = "/"