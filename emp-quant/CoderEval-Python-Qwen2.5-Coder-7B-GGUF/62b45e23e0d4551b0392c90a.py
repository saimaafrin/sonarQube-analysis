def validate_version_inventories(self, version_dirs):
    root_inventory = self.load_inventory('root')
    content_digests = set()

    for version_dir in version_dirs:
        version_inventory = self.load_inventory(version_dir)
        if not version_inventory:
            raise ValueError(f"No inventory found for version: {version_dir}")

        for content_id, content_info in version_inventory.items():
            if content_id not in root_inventory:
                content_digests.add(content_info['digest'])

        if version_dir != 'root':
            if not root_inventory.is_subset(version_inventory):
                raise ValueError(f"Version {version_dir} does not contain all contents of previous versions")

    return content_digests