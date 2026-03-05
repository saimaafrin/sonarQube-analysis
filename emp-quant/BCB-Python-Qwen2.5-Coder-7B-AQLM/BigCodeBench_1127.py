
import os
import re
import hashlib

def task_func(path, delimiter):
    def compute_hash(file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            return file_hash
        else:
            return None

    # Split the path by the specified delimiter
    components = re.split(re.escape(delimiter), path)

    # Compute the hash for each component if it is a file
    result = [(component, compute_hash(component)) for component in components]

    return result