def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if extract_spec_version:
		if inventory.get('type') is not None:
			if inventory['type'] in self.spec_versions:
				self.spec_version = self.spec_versions[inventory['type']]
			else:
				self.spec_version = self.spec_versions['default']
		else:
			self.spec_version = self.spec_versions['default']

	if self.spec_version == '1.0':
		self.validate_v1_0(inventory)
	elif self.spec_version == '1.1':
		self.validate_v1_1(inventory)
	elif self.spec_version == '1.2':
		self.validate_v1_2(inventory)
	elif self.spec_version == '2.0':
		self.validate_v2_0(inventory)
	elif self.spec_version == '2.1':
		self.validate_v2_1(inventory)
	elif self.spec_version == '2.2':
		self.validate_v2_2(inventory)
	else:
		raise Exception('Unsupported specification version: %s' % self.spec_version)