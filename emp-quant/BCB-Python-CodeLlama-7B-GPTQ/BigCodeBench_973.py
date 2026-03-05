import os
import shutil
def task_func(path, delimiter="/"):
    """
    Splits a given file path by a specific delimiter and computes disk usage for each directory component.
    """
    # Check if the path is empty, not a string, or contain invalid components
    if not path or not isinstance(path, str):
        raise ValueError("Invalid path")
    # Check if the path exists in the filesystem
    if not os.path.exists(path):
        raise FileNotFoundError("Path does not exist")
    # Split the path by the delimiter
    path_components = path.split(delimiter)
    # Compute disk usage for each directory component
    disk_usage = []
    for component in path_components:
        try:
            du = shutil.disk_usage(component)
            disk_usage.append((component, {"total": du.total, "used": du.used, "free": du.free}))
        except FileNotFoundError:
            disk_usage.append((component, {"total": 0, "used": 0, "free": 0}))
    return disk_usage
path = "a/b/c"
delimiter = "/"