def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if path == "/":
		return True
	elif path.startswith("/"):
		path = path[1:]
	if path.endswith("/"):
		path = path[:-1]
	if path.startswith("."):
		return False
	if path.startswith("_"):
		return False
	if path.startswith("~"):
		return False
	if path.startswith(".."):
		return False
	if path.startswith("."):
		return False
	if path.startswith("_"):
		return False
	if path.startswith("~"):
		return False
	if path.startswith(".."):
		return False
	if path.startswith("."):
		return False
	if path.startswith("_"):
		return False
	if path.startswith("~"):
		return False
	if path.startswith(".."):
		return False
	if path.startswith("."):
		return False
	if path.startswith("_"):
		return False
	if path.startswith("~"):
		return False
	if path.startswith(".."):
		return False
	if path.startswith("."):
		return False
	if path.startswith("_"):
		return False
	if path.startswith("~"):
		return False
	if path.startswith(".."):
		return False
	if path.startswith("."):
		return False
	if path.startswith("_"):
		return False
	if path.startswith("~"):
		return False
	if path.startswith(".."):
		return False
	if path.startswith("."):
		return False
	if path.startswith("_"):
		return False
	if path.startswith("~"):
		return False
	if path.startswith(".."):
		return False
	if path.startswith("."):
		return False
	if path.startswith("_"):
		return