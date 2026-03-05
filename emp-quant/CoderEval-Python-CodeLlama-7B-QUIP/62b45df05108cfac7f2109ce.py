def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if not path:
		path = self.root
	if not self.exists(path):
		return False
	if self.is_dir(path):
		return False
	return True