def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	root_inventory = self.get_root_inventory()
	root_content_digests = root_inventory.get_content_digests()
	root_content_digests_by_version = {}
	for version_dir in version_dirs:
		version_inventory = self.get_version_inventory(version_dir)
		version_content_digests = version_inventory.get_content_digests()
		root_content_digests_by_version[version_dir] = version_content_digests
		for content_digest in version_content_digests:
			if content_digest not in root_content_digests:
				raise ValidationError("Version inventory for version %s contains content digest %s that is not in the root inventory" % (version_dir, content_digest))
			if root_content_digests[content_digest] != version_content_digests[content_digest]:
				raise ValidationError("Version inventory for version %s contains content digest %s with a different digest than the root inventory" % (version_dir, content_digest))
	return root_content_digests_by_version