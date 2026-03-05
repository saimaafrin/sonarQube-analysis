
import os
import shutil

def task_func(path, delimiter="/"):
    if not isinstance(path, str) or not path:
        raise ValueError("Invalid path")
    
    if not os.path.exists(path):
        raise FileNotFoundError("Path does not exist")
    
    components = path.split(delimiter)
    disk_usage = []
    
    for component in components:
        component_path = os.path.join(*components[:components.index(component) + 1])
        usage = shutil.disk_usage(component_path)
        disk_usage.append((component, {'total': usage.total, 'used': usage.used, 'free': usage.free}))
    
    return disk_usage