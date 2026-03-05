def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if extract_spec_version:
		if 'type' in inventory:
			if inventory['type'] in self.spec_versions:
				self.spec_version = self.spec_versions[inventory['type']]
			else:
				raise ValueError('Invalid type value: ' + inventory['type'])
		else:
			raise ValueError('Missing type value')
	else:
		self.spec_version = self.spec_versions[self.spec_version]
	if 'id' not in inventory:
		raise ValueError('Missing id value')
	if 'type' not in inventory:
		raise ValueError('Missing type value')
	if inventory['type'] not in self.spec_versions:
		raise ValueError('Invalid type value: ' + inventory['type'])
	if 'version' not in inventory:
		raise ValueError('Missing version value')
	if inventory['version'] not in self.spec_versions[inventory['type']]:
		raise ValueError('Invalid version value: ' + inventory['version'])
	if 'name' not in inventory:
		raise ValueError('Missing name value')
	if 'description' not in inventory:
		raise ValueError('Missing description value')
	if 'license' not in inventory:
		raise ValueError('Missing license value')
	if 'license' in inventory and inventory['license'] not in self.licenses:
		raise ValueError('Invalid license value: ' + inventory['license'])
	if 'authors' not in inventory:
		raise ValueError('Missing authors value')
	if 'authors' in inventory and len(inventory['authors']) == 0:
		raise ValueError('Invalid authors value: ' + inventory['authors'])
	if 'maintainers' not in inventory:
		raise ValueError('Missing maintainers value')
	if 'maintainers' in inventory and len(inventory['maintainers']) == 0:
		raise ValueError('Invalid maintain