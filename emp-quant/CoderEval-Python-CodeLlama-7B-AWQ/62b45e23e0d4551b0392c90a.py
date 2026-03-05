def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	root_inventory = self.get_root_inventory()
	root_content_digests = root_inventory['content_digests']
	root_content_digests_by_version = {}
	for version_dir in version_dirs:
		version_inventory = self.get_version_inventory(version_dir)
		version_content_digests = version_inventory['content_digests']
		for content_digest in version_content_digests:
			if content_digest not in root_content_digests:
				root_content_digests.append(content_digest)
				root_content_digests_by_version[content_digest] = version_dir
	self.set_root_inventory(root_inventory)
	self.set_root_content_digests_by_version(root_content_digests_by_version)