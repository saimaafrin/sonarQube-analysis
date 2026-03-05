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
        # Get the current component
        component = components[i]
        
        # Check if the component is a file
        if os.path.isfile(component):
            # Compute the hash of the file
            with open(component, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
        else:
            # If it's not a file, set the hash to None
            file_hash = None
        
        # Append the component and its hash to the result list
        result.append((component, file_hash))
    
    # Return the result list
    return result