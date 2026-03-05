
import os
import re
import hashlib
def task_func(path, delimiter):
    # Split the path by the delimiter
    components = path.split(delimiter)
    
    # Initialize a list to store the result
    result = []
    
    # Iterate over the components
    for component in components:
        # Check if the component is a file
        if os.path.isfile(component):
            # Compute the hash of the file
            with open(component, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            result.append((component, file_hash))
        else:
            # If not a file, append the component with None as the hash
            result.append((component, None))
    
    return result