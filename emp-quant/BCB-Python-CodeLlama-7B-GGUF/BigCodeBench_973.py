
import os
import shutil

def task_func(path, delimiter="/"):
    if not path or not isinstance(path, str):
        raise ValueError("Invalid path")
    if not os.path.exists(path):
        raise FileNotFoundError("Path does not exist")

    components = path.split(delimiter)
    disk_usage = []
    for component in components:
        usage = shutil.disk_usage(component)
        disk_usage.append((component, {"total": usage.total, "used": usage.used, "free": usage.free}))

    return disk_usage