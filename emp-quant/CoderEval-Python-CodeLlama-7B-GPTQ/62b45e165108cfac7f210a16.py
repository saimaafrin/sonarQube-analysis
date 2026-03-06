def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if prior.get_version() != self.get_version():
		self.error("Prior version is not the same as current version.")
		return
	if prior.get_num_items() != self.get_num_items():
		self.error("Prior version has different number of items than current version.")
		return
	if prior.get_num_items() == 0:
		return
	if prior.get_item_type(0) != self.get_item_type(0):
		self.error("Prior version has different item type than current version.")
		return
	if prior.get_item_type(0) == "file":
		if prior.get_file_size(0) != self.get_file_size(0):
			self.error("Prior version has different file size than current version.")
			return
		if prior.get_file_hash(0) != self.get_file_hash(0):
			self.error("Prior version has different file hash than current version.")
			return
		if prior.get_file_name(0) != self.get_file_name(0):
			self.error("Prior version has different file name than current version.")
			return
		if prior.get_file_path(0) != self.get_file_path(0):
			self.error("Prior version has different file path than current version.")
			return
		if prior.get_file_permissions(0) != self.get_file_permissions(0):
			self.error("Prior version has different file permissions than current version.")
			return
		if prior.get_file_owner(0) != self.get_file_owner(0):
			self.error("Prior version has different file owner than current version.")
			return
		if prior.get_file_group(0) != self.get_file_group(0):
			self.error("Prior version has different file group than current version.")
			return
		if prior.