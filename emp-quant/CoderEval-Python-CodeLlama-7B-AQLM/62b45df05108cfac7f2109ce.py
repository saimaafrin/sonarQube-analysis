def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if path == "/":
		return True
	else:
		return self.fs.exists(path)