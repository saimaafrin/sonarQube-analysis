import os

def validate(self, path):
    """
    Returns True if OCFL object at path or pyfs root, False otherwise.
    """
    return os.path.exists(path) and self.is_ocfl_object(path)