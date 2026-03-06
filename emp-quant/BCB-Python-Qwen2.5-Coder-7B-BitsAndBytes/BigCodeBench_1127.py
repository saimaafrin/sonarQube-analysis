
import os
import re
import hashlib

def task_func(path, delimiter):
    def compute_file_hash(file_path):
        """Compute the SHA-256 hash of a file."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            buf = f.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()

    # Split the path using the specified delimiter
    components = re.split(re.escape(delimiter), path)

    result = []
    for component in components:
        full_path = os.path.join(os.getcwd(), component)
        if os.path.isfile(full_path):
            file_hash = compute_file_hash(full_path)
        else:
            file_hash = None
        result.append((component, file_hash))

    return result