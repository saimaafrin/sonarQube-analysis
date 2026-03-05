def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	# Check that each version has an inventory up to that point
	for version_dir in version_dirs:
		version_inventory_path = os.path.join(self.root_dir, version_dir, 'inventory.json')
		if not os.path.exists(version_inventory_path):
			raise Exception('Version %s does not have an inventory' % version_dir)

	# Check that each version has the same content digests as the root inventory
	root_inventory = self.get_inventory()
	for version_dir in version_dirs:
		version_inventory = self.get_inventory(version_dir)
		for content_digest in version_inventory['content_digests']:
			if content_digest not in root_inventory['content_digests']:
				raise Exception('Version %s has a content digest %s that is not in the root inventory' % (version_dir, content_digest))

	# Check that each version has the same content digests as the previous version
	for i in range(len(version_dirs)-1):
		version_dir = version_dirs[i]
		previous_version_dir = version_dirs[i+1]
		version_inventory = self.get_inventory(version_dir)
		previous_version_inventory = self.get_inventory(previous_version_dir)
		for content_digest in version_inventory['content_digests']:
			if content_digest not in previous_version_inventory['content_digests']:
				raise Exception('Version %s has a content digest %s that is not in the previous version %s' % (version_dir, content_digest, previous_version_dir))

	# Check that each version has the same content digests as the next version
	for i in range(len(version_dirs)-1):
		version_dir = version_dirs[i]
		next_version_dir = version_dirs[i+1]
		version_inventory =