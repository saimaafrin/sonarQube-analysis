import os

class OCFLStorage:
    def __init__(self, root_path):
        self.root_path = root_path

    def initialize(self):
        """
        Create and initialize a new OCFL storage root.
        """
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)
        else:
            raise FileExistsError(f"The directory {self.root_path} already exists.")
        
        # Initialize necessary subdirectories
        for subdir in ['objects', 'manifests', 'versions']:
            os.makedirs(os.path.join(self.root_path, subdir), exist_ok=True)

        print(f"OCFL storage root initialized at {self.root_path}")