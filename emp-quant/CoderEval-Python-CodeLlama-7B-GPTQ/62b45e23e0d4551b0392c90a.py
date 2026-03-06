def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	root_inventory = self.get_root_inventory()
	root_digests = root_inventory.get_content_digests()
	root_digests_by_version = {}
	for version_dir in version_dirs:
		version_inventory = self.get_version_inventory(version_dir)
		version_digests = version_inventory.get_content_digests()
		root_digests_by_version[version_dir] = version_digests
		if version_digests != root_digests:
			raise Exception("Version %s has different content digests than root inventory" % version_dir)

	return root_digests_by_version