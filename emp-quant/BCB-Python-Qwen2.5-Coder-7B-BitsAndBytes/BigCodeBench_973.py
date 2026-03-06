
import os
import shutil

def task_func(path, delimiter="/"):
    if not isinstance(path, str) or not path:
        raise ValueError("Path must be a non-empty string.")
    
    if delimiter not in path:
        raise ValueError(f"Delimiter '{delimiter}' not found in the path.")
    
    components = path.split(delimiter)
    result = []
    
    for i in range(len(components)):
        current_path = delimiter.join(components[:i+1])
        try:
            total, used, free = shutil.disk_usage(current_path)
            result.append((components[i], {
                'total': total,
                'used': used,
                'free': free
            }))
        except FileNotFoundError:
            raise FileNotFoundError(f"The path '{current_path}' does not exist.")
    
    return result