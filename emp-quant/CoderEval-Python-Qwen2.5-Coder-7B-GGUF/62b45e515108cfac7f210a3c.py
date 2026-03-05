import os

def initialize(self):
    """
    Create and initialize a new OCFL storage root.
    """
    if not os.path.exists(self.root):
        os.makedirs(self.root)
        with open(os.path.join(self.root, 'manifest.json'), 'w') as f:
            f.write('{}')
        with open(os.path.join(self.root, 'inventory.json'), 'w') as f:
            f.write('{}')
        with open(os.path.join(self.root, 'config.json'), 'w') as f:
            f.write('{"version": "1.0"}')