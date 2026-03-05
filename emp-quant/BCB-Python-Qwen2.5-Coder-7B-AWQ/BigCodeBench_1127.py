import os
import re
import hashlib
def task_func(path, delimiter):
    # Split the path by the specified delimiter
    components = re.split(f'({re.escape(delimiter)})', path)
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the components
    for i in range(0, len(components), 2):
        # Get the current component and the next delimiter
        component = components[i]
        next_delimiter = components[i + 1] if i + 1 < len(components) else ''
        
        # Check if the current component is a file
        if os.path.isfile(component):
            # Compute the hash of the file
            with open(component, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
        else:
            # If it's not a file, set the hash to None
            file_hash = None
        
        # Append the component and its hash to the result list
        result.append((component + next_delimiter, file_hash))
    
    return result