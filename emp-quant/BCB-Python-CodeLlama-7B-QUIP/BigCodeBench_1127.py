
import os
import re
import hashlib

def task_func(path, delimiter):
    # Split the path by the delimiter
    components = path.split(delimiter)

    # Compute the hash of each component
    hashes = []
    for component in components:
        if os.path.isfile(component):
            # If the component is a file, compute its hash
            with open(component, 'rb') as f:
                hash = hashlib.sha256(f.read()).hexdigest()
            hashes.append((component, hash))
        else:
            # If the component is not a file, its hash will be None
            hashes.append((component, None))

    return hashes