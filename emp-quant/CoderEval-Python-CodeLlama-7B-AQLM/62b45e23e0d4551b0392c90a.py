def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	# Check that each version has an inventory
	for version_dir in version_dirs:
		version_inventory_path = os.path.join(self.root_dir, version_dir, 'inventory.json')
		if not os.path.exists(version_inventory_path):
			raise Exception('Version %s does not have an inventory' % version_dir)

	# Check that each version has a content digest
	for version_dir in version_dirs:
		version_inventory_path = os.path.join(self.root_dir, version_dir, 'inventory.json')
		version_inventory = json.load(open(version_inventory_path))
		if 'content_digest' not in version_inventory:
			raise Exception('Version %s does not have a content digest' % version_dir)

	# Check that each version has a content digest that matches the root inventory
	root_inventory = json.load(open(os.path.join(self.root_dir, 'inventory.json')))
	for version_dir in version_dirs:
		version_inventory_path = os.path.join(self.root_dir, version_dir, 'inventory.json')
		version_inventory = json.load(open(version_inventory_path))
		if version_inventory['content_digest'] != root_inventory['content_digest']:
			raise Exception('Version %s content digest does not match root inventory' % version_dir)

	# Check that each version has a content digest that matches the previous version
	for i in range(len(version_dirs) - 1):
		version_dir = version_dirs[i]
		version_inventory_path = os.path.join(self.root_dir, version_dir, 'inventory.json')
		version_inventory = json.load(open(version_inventory_path))
		if version_inventory['content_digest'] != version_dirs[i + 1]:
			raise Exception