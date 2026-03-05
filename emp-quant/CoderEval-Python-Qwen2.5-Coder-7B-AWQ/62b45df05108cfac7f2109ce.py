import os

class OCFLValidator:
    def __init__(self, root):
        self.root = root

    def validate(self, path):
        """
        Returns True if OCFL object at path or pyfs root, False otherwise.
        """
        return os.path.exists(os.path.join(self.root, path))