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
	if self.spec_version == '1.0':
		self.validate_v1_0(inventory)
	elif self.spec_version == '1.1':
		self.validate_v1_1(inventory)
	elif self.spec_version == '1.2':
		self.validate_v1_2(inventory)
	elif self.spec_version == '1.3':
		self.validate_v1_3(inventory)
	elif self.spec_version == '1.4':
		self.validate_v1_4(inventory)
	elif self.spec_version == '1.5':
		self.validate_v1_5(inventory)
	elif self.spec_version == '1.6':
		self.validate_v1_6(inventory)
	elif self.spec_version == '1.7':
		self.validate_v1_7(inventory)
	elif self.spec_version == '1.8':
		self.validate_v1_8(inventory)
	elif self.spec_version == '1.9':
		self.validate_v1_9(inventory)
	elif self.spec_version == '1.10':
		self.validate_v1_10(inventory)
	elif self.spec_version == '1.11':
		self.validate_v1_11(inventory)
	elif self.spec_version == '1.12':
		self.validate_v1_12(inventory)
	elif self.spec_version == '1.13':
		self.validate_v