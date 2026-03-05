import os
import shutil
def task_func(path, delimiter="/"):
    if not isinstance(path, str) or not path:
        raise ValueError("The 'path' must be a non-empty string.")
    
    if delimiter not in path:
        raise ValueError("The 'delimiter' must be present in the 'path'.")
    
    if not os.path.exists(path):
        raise FileNotFoundError("The 'path' does not exist in the filesystem.")
    
    components = path.split(delimiter)
    disk_usage = []
    
    for i in range(1, len(components) + 1):
        current_path = delimiter.join(components[:i])
        total, used, free = shutil.disk_usage(current_path)
        disk_usage.append((current_path, {'total': total, 'used': used, 'free': free}))
    
    return disk_usage