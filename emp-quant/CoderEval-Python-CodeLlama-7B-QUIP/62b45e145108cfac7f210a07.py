def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	# Check for required fields
	if not inventory.get('id'):
		raise ValidationException("Inventory must have an id")
	if not inventory.get('name'):
		raise ValidationException("Inventory must have a name")
	if not inventory.get('type'):
		raise ValidationException("Inventory must have a type")
	if not inventory.get('version'):
		raise ValidationException("Inventory must have a version")
	if not inventory.get('spec_version'):
		raise ValidationException("Inventory must have a spec_version")
	if not inventory.get('created_at'):
		raise ValidationException("Inventory must have a created_at")
	if not inventory.get('updated_at'):
		raise ValidationException("Inventory must have an updated_at")
	if not inventory.get('created_by'):
		raise ValidationException("Inventory must have a created_by")
	if not inventory.get('updated_by'):
		raise ValidationException("Inventory must have an updated_by")
	if not inventory.get('status'):
		raise ValidationException("Inventory must have a status")
	if not inventory.get('description'):
		raise ValidationException("Inventory must have a description")
	if not inventory.get('description').get('id'):
		raise ValidationException("Inventory must have a description with an id")
	if not inventory.get('description').get('name'):
		raise ValidationException("Inventory must have a description with a name")
	if not inventory.get('description').get('type'):
		raise ValidationException("Inventory must have a description with a type")
	if not inventory.get('description').get('version'):
		raise ValidationException("Inventory must have a description with a version")
	if not inventory.get('description').get('spec_version'):
		raise ValidationException("Inventory must have a description with a spec_version")
	if not inventory.get('description').get('created_at'):
		raise ValidationException("Inventory must have a description with