import os

class VersionInventoryValidator:
    def __init__(self, root_inventory_path):
        self.root_inventory = self.load_inventory(root_inventory_path)
        self.digest_records = {}

    def load_inventory(self, path):
        with open(path, 'r') as file:
            return {line.split()[0]: line.split()[1] for line in file}

    def validate_version_inventories(self, version_dirs):
        for version_dir in version_dirs:
            version_inventory_path = os.path.join(version_dir, 'inventory.txt')
            if not os.path.exists(version_inventory_path):
                raise ValueError(f"Inventory file missing for version: {version_dir}")

            version_inventory = self.load_inventory(version_inventory_path)

            for item, digest in version_inventory.items():
                if item not in self.root_inventory or self.root_inventory[item] != digest:
                    self.digest_records[item] = digest

        return self.digest_records