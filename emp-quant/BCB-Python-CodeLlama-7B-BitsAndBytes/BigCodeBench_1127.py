
import os
import re
import hashlib

def task_func(path, delimiter):
    # Split the path by the specified delimiter
    path_components = path.split(delimiter)

    # Compute the hash of each component that is a file
    hashes = []
    for component in path_components:
        if os.path.isfile(component):
            with open(component, 'rb') as f:
                hashes.append((component, hashlib.sha256(f.read()).hexdigest()))
        else:
            hashes.append((component, None))

    return hashes