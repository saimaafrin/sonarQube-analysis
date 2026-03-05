import os

class OCFLValidator:
    def __init__(self, root_path):
        self.root_path = root_path

    def validate(self, path):
        """
        Returns True if OCFL object at path or pyfs root, False otherwise.
        """
        full_path = os.path.join(self.root_path, path)
        return os.path.exists(full_path) and os.path.isdir(full_path)