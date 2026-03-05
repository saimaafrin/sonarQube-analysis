import os

def find_path_type(path):
    if os.path.isfile(path):
        return "file"
    elif os.path.isdir(path):
        return "directory"
    elif os.path.islink(path):
        return "link"
    else:
        return "unknown"