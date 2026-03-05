import os

class VersionInventoryValidator:
    def __init__(self, root_inventory_path):
        self.root_inventory = self.load_inventory(root_inventory_path)
        self.different_content_digests = set()

    def load_inventory(self, path):
        with open(path, 'r') as file:
            return {line.strip() for line in file}

    def validate_version_inventories(self, version_dirs):
        for version_dir in version_dirs:
            version_inventory_path = os.path.join(version_dir, 'inventory.txt')
            if not os.path.exists(version_inventory_path):
                raise ValueError(f"Inventory file missing for version: {version_dir}")

            version_inventory = self.load_inventory(version_inventory_path)

            for item in version_inventory:
                if item not in self.root_inventory:
                    self.different_content_digests.add(item)

        return self.different_content_digests