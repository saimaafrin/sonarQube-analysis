
import os
import shutil

def task_func(path, delimiter="/"):
    if not path:
        raise ValueError("Path is empty")
    if not isinstance(path, str):
        raise ValueError("Path is not a string")
    if not delimiter in path:
        raise ValueError("Path does not contain delimiter")
    if not os.path.exists(path):
        raise FileNotFoundError("Path does not exist in the filesystem")

    components = path.split(delimiter)
    disk_usage = []
    for component in components:
        component_path = delimiter.join(components[:i])
        try:
            usage = shutil.disk_usage(component_path)
            disk_usage.append((component, usage))
        except FileNotFoundError:
            continue
    return disk_usage