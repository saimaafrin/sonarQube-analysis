def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if self.version != prior.version:
		self.error("Inventory version mismatch: %s != %s" % (self.version, prior.version))
	if self.name != prior.name:
		self.error("Inventory name mismatch: %s != %s" % (self.name, prior.name))
	if self.description != prior.description:
		self.error("Inventory description mismatch: %s != %s" % (self.description, prior.description))
	if self.date != prior.date:
		self.error("Inventory date mismatch: %s != %s" % (self.date, prior.date))
	if self.location != prior.location:
		self.error("Inventory location mismatch: %s != %s" % (self.location, prior.location))
	if self.contact != prior.contact:
		self.error("Inventory contact mismatch: %s != %s" % (self.contact, prior.contact))
	if self.url != prior.url:
		self.error("Inventory url mismatch: %s != %s" % (self.url, prior.url))
	if self.license != prior.license:
		self.error("Inventory license mismatch: %s != %s" % (self.license, prior.license))
	if self.license_url != prior.license_url:
		self.error("Inventory license_url mismatch: %s != %s" % (self.license_url, prior.license_url))
	if self.notes != prior.notes:
		self.error("Inventory notes mismatch: %s != %s" % (self.notes, prior.notes))
	if self.tags != prior.tags:
		self.error("Inventory tags mismatch: %s != %s" % (self.tags, prior.tags))
	if self.inventory_type != prior.inventory_type:
		self.error("Inventory inventory_type mismatch: %s != %s" % (self.inventory_type, prior.inventory_type))
	if self.inventory_type_version != prior