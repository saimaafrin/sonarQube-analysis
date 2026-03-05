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
            # Initialize necessary files and directories for OCFL storage
            ocfl_root_dir = os.path.join(self.root_path, 'ocfl')
            os.makedirs(ocfl_root_dir)
            inventory_file = os.path.join(ocfl_root_dir, 'inventory.json')
            with open(inventory_file, 'w') as f:
                f.write('{}')
            print(f"OCFL storage initialized at {self.root_path}")
        else:
            print(f"OCFL storage already exists at {self.root_path}")