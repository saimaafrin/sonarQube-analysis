def validate_version_inventories(self, version_dirs):
    root_inventory = self.get_root_inventory()
    content_digests = set()

    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, 'inventory')
        if not os.path.exists(inventory_path):
            raise ValueError(f"Inventory for version {version_dir} does not exist.")

        version_inventory = self.load_inventory(inventory_path)
        if version_inventory != root_inventory:
            content_digests.update(version_inventory.difference(root_inventory))

    return content_digests