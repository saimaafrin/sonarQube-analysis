import os
import shutil
def task_func(path, delimiter="/"):
    # Check if the path is empty or not a string
    if not path or not isinstance(path, str):
        raise ValueError("The 'path' must be a non-empty string.")
    
    # Split the path by the delimiter
    components = path.split(delimiter)
    
    # Check if the path contains invalid components
    if not all(c for c in components if c):
        raise ValueError("The 'path' contains invalid components.")
    
    # Initialize the result list
    result = []
    
    # Iterate over the components and compute disk usage
    for i in range(1, len(components) + 1):
        current_path = delimiter.join(components[:i])
        try:
            # Get disk usage statistics
            total, used, free = shutil.disk_usage(current_path)
            result.append((current_path, {'total': total, 'used': used, 'free': free}))
        except FileNotFoundError:
            raise FileNotFoundError(f"The 'path' does not exist in the filesystem: {current_path}")
    
    return result