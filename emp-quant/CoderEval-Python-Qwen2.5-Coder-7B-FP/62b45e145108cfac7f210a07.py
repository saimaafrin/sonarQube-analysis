def validate(self, inventory, extract_spec_version=False):
# Check if the inventory is empty
	if not inventory:
		return False

	# Extract the specification version from the inventory if required
	if extract_spec_version:
		type_value = inventory.get('type')
		if type_value and type_value in ['v1', 'v2']:
			self.spec_version = type_value
		else:
			self.spec_version = 'default'

	# Validate the inventory based on the specification version
	if self.spec_version == 'v1':
		return self.validate_v1(inventory)
	elif self.spec_version == 'v2':
		return self.validate_v2(inventory)
	else:
		return self.validate_default(inventory)