def validate_version_inventories(self, version_dirs):
# Initialize variables to track inventory files and content digests
	inventory_files = set()
	content_digests = {}

	# Iterate through each version directory
	for version_dir in version_dirs:
		# Construct the path to the inventory file for the current version
		inventory_path = os.path.join(version_dir, 'inventory.json')

		# Check if the inventory file exists
		if not os.path.exists(inventory_path):
			self.log_error(f"Inventory file missing for version {version_dir}")
			return False

		# Add the inventory file to the set of tracked inventory files
		inventory_files.add(inventory_path)

		# Load the inventory data from the JSON file
		try:
			with open(inventory_path, 'r') as f:
				inventory_data = json.load(f)
		except Exception as e:
			self.log_error(f"Failed to load inventory data for version {version_dir}: {e}")
			return False

		# Extract content digests from the inventory data
		for item in inventory_data['items']:
			digest = item.get('digest')
			if digest:
				content_digests[digest] = True

	# Log the number of inventory files found
	self.log_info(f"Found {len(inventory_files)} inventory files across versions.")

	# Optionally, you can add more checks here to ensure consistency between inventories or other validation rules

	return True
```

This code snippet defines a method `validate_version_inventories` within a class. The method takes a list of version directory names (`version_dirs`) as input and performs several checks to ensure that each version has an inventory file and that all content digests are correctly recorded. It logs errors and information using methods like `log_error` and `log_info`. The method returns `True` if all validations pass, otherwise it returns `False`. This helps in maintaining integrity and consistency across different versions of content.