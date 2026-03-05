
import os
import shutil

def task_func(path, delimiter="/"):
    if not isinstance(path, str) or not path:
        raise ValueError("The 'path' must be a non-empty string.")
    
    if delimiter not in path:
        raise ValueError("The 'path' must contain the specified delimiter.")
    
    if not os.path.exists(path):
        raise FileNotFoundError("The 'path' does not exist in the filesystem.")
    
    components = path.split(delimiter)
    disk_usage = []
    
    for i in range(len(components)):
        component_path = delimiter.join(components[:i+1])
        try:
            total, used, free = shutil.disk_usage(component_path)
            disk_usage.append((component_path, {'total': total, 'used': used, 'free': free}))
        except PermissionError:
            disk_usage.append((component_path, {'total': None, 'used': None, 'free': None}))
    
    return disk_usage