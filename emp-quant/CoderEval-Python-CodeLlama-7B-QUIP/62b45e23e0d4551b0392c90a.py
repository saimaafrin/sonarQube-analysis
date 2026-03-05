def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	inventory_dir = self.get_inventory_dir()
	inventory_file = os.path.join(inventory_dir, "inventory.json")
	inventory = self.get_inventory(inventory_file)
	inventory_content_digests = inventory["content_digests"]
	inventory_content_digests_by_version = {}
	for version_dir in version_dirs:
		version_dir_path = os.path.join(self.get_version_dir(), version_dir)
		version_inventory_file = os.path.join(version_dir_path, "inventory.json")
		version_inventory = self.get_inventory(version_inventory_file)
		version_content_digests = version_inventory["content_digests"]
		inventory_content_digests_by_version[version_dir] = version_content_digests
		for content_digest in version_content_digests:
			if content_digest not in inventory_content_digests:
				self.fail("Version %s inventory does not contain content digest %s" % (version_dir, content_digest))
			if inventory_content_digests[content_digest] != version_inventory["content_digests"][content_digest]:
				self.fail("Version %s inventory content digest %s does not match root inventory content digest %s" % (version_dir, content_digest, inventory_content_digests[content_digest]))
	return inventory_content_digests_by_version