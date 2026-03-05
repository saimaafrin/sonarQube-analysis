def values(self, *keys):
	"""
	Returns the key filtered by self.index in the form of a list.
	"""
	return [self.index[k] for k in keys]