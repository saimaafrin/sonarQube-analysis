def validate_version_inventories(self, version_dirs):
    """
    Each version SHOULD have an inventory up to that point.

    Also keep a record of any content digests different from those in the root inventory
    so that we can also check them when validating the content.

    version_dirs is an array of version directory names and is assumed to be in
    version sequence (1, 2, 3...).
    """
    root_inventory = self.get_root_inventory()
    content_digests = {}

    for version_dir in version_dirs:
        inventory = self.get_inventory(version_dir)
        if inventory is None:
            raise ValueError(f"No inventory found for version {version_dir}")

        for content_id, content_digest in inventory.items():
            if content_id not in root_inventory or root_inventory[content_id] != content_digest:
                content_digests[content_id] = content_digest

    return content_digests