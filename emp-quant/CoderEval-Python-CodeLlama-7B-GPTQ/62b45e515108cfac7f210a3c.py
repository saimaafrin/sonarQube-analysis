def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	self.storage_root = StorageRoot(self.storage_root_path)
	self.storage_root.initialize()