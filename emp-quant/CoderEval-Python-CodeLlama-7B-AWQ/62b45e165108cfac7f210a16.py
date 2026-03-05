def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if prior.get_version() != self.get_version() - 1:
		self.error("Prior version is not one less than current version.")
	if prior.get_date() > self.get_date():
		self.error("Prior version is not earlier than current version.")
	if prior.get_date() == self.get_date():
		if prior.get_version() != self.get_version() - 1:
			self.error("Prior version is not one less than current version.")
	if prior.get_date() < self.get_date():
		if prior.get_version() != self.get_version() - 2:
			self.error("Prior version is not two less than current version.")
	if prior.get_date() == self.get_date() and prior.get_version() == self.get_version() - 1:
		if not self.get_date() == self.get_date():
			self.error("Prior version is not one less than current version.")
	if prior.get_date() == self.get_date() and prior.get_version() == self.get_version() - 2:
		if not self.get_date() == self.get_date():
			self.error("Prior version is not two less than current version.")
	if prior.get_date() == self.get_date() and prior.get_version() == self.get_version() - 3:
		if not self.get_date() == self.get_date():
			self.error("Prior version is not three less than current version.")
	if prior.get_date() == self.get_date() and prior.get_version() == self.get_version() - 4:
		if not self.get_date() == self.get_date():
			self.error("Prior version is not four less than current version.")
	if prior.get_date() == self.get_date() and prior.get_version() == self.get_version() - 5:
		if not self.get_date() == self