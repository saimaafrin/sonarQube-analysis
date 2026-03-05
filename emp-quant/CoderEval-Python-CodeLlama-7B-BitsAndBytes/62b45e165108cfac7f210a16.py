def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if self.version != prior.version:
		self.error("Inventory version mismatch: %s != %s" % (self.version, prior.version))
		return
	if self.inventory_id != prior.inventory_id:
		self.error("Inventory ID mismatch: %s != %s" % (self.inventory_id, prior.inventory_id))
		return
	if self.inventory_name != prior.inventory_name:
		self.error("Inventory name mismatch: %s != %s" % (self.inventory_name, prior.inventory_name))
		return
	if self.inventory_description != prior.inventory_description:
		self.error("Inventory description mismatch: %s != %s" % (self.inventory_description, prior.inventory_description))
		return
	if self.inventory_type != prior.inventory_type:
		self.error("Inventory type mismatch: %s != %s" % (self.inventory_type, prior.inventory_type))
		return
	if self.inventory_status != prior.inventory_status:
		self.error("Inventory status mismatch: %s != %s" % (self.inventory_status, prior.inventory_status))
		return
	if self.inventory_status_date != prior.inventory_status_date:
		self.error("Inventory status date mismatch: %s != %s" % (self.inventory_status_date, prior.inventory_status_date))
		return
	if self.inventory_status_reason != prior.inventory_status_reason:
		self.error("Inventory status reason mismatch: %s != %s" % (self.inventory_status_reason, prior.inventory_status_reason))
		return
	if self.inventory_status_resolution != prior.inventory_status_resolution:
		self.error("Inventory status resolution mismatch: %s != %s" % (self.inventory_status_resolution, prior.inventory_status_resolution))
		return