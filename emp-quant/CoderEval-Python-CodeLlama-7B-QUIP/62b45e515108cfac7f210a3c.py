def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	self.root = OCFLRoot(self.root_path)
	self.root.initialize()