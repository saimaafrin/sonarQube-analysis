import os

def validate(self, path):
    """
    Returns True if OCFL object at path or pyfs root, False otherwise.
    """
    if os.path.exists(path):
        return True
    else:
        return False