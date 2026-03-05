import os

def validate_version_inventories(self, version_dirs):
    root_inventory = self.load_inventory('root')
    content_digests = set()

    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, 'inventory')
        if not os.path.exists(inventory_path):
            raise ValueError(f"Inventory file missing for version {version_dir}")

        inventory = self.load_inventory(version_dir)
        for item, digest in inventory.items():
            if item not in root_inventory or digest != root_inventory[item]:
                content_digests.add(digest)

    return content_digests