def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if self.get_version() != prior.get_version():
		self.error("Inventory version mismatch: %s != %s" % (self.get_version(), prior.get_version()))
		return
	if self.get_name() != prior.get_name():
		self.error("Inventory name mismatch: %s != %s" % (self.get_name(), prior.get_name()))
		return
	if self.get_description() != prior.get_description():
		self.error("Inventory description mismatch: %s != %s" % (self.get_description(), prior.get_description()))
		return
	if self.get_date() != prior.get_date():
		self.error("Inventory date mismatch: %s != %s" % (self.get_date(), prior.get_date()))
		return
	if self.get_time() != prior.get_time():
		self.error("Inventory time mismatch: %s != %s" % (self.get_time(), prior.get_time()))
		return
	if self.get_location() != prior.get_location():
		self.error("Inventory location mismatch: %s != %s" % (self.get_location(), prior.get_location()))
		return
	if self.get_location_type() != prior.get_location_type():
		self.error("Inventory location type mismatch: %s != %s" % (self.get_location_type(), prior.get_location_type()))
		return
	if self.get_location_id() != prior.get_location_id():
		self.error("Inventory location id mismatch: %s != %s" % (self.get_location_id(), prior.get_location_id()))
		return
	if self.get_location_name() != prior.get_location_name():
		self.error("Inventory location name mismatch: %s != %s" % (self.get_location_name(), prior.get_location_name()))
		return
	if self.get_location_description() != prior.get_location_description