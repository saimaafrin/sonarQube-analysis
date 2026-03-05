
import os
import re
import hashlib

def task_func(path, delimiter):
    def compute_file_hash(file_path):
        """Compute the SHA-256 hash of a file."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            buf = f.read(65536)
            while buf:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()

    # Split the path by the specified delimiter
    components = re.split(re.escape(delimiter), path)
    
    result = []
    for component in components:
        # Check if the component is a file
        if os.path.isfile(component):
            # Compute the hash of the file
            file_hash = compute_file_hash(component)
        else:
            file_hash = None
        
        # Append the component and its hash to the result list
        result.append((component, file_hash))
    
    return result