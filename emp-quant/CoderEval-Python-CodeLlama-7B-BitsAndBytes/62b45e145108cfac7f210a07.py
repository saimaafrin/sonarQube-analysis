def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if extract_spec_version:
		if 'type' in inventory:
			if inventory['type'] in self.spec_versions:
				self.spec_version = self.spec_versions[inventory['type']]
			else:
				self.spec_version = self.spec_versions['default']
		else:
			self.spec_version = self.spec_versions['default']
	self.validate_inventory(inventory)