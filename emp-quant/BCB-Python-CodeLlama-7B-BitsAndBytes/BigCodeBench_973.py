
import os
import shutil

def task_func(path, delimiter="/"):
    if not isinstance(path, str) or not path:
        raise ValueError("Invalid path")
    if not os.path.exists(path):
        raise FileNotFoundError("Path does not exist")

    # Split the path by the delimiter
    path_components = path.split(delimiter)

    # Compute the disk usage for each component
    disk_usage = []
    for component in path_components:
        try:
            usage = shutil.disk_usage(component)
            disk_usage.append((component, usage))
        except OSError:
            pass

    return disk_usage