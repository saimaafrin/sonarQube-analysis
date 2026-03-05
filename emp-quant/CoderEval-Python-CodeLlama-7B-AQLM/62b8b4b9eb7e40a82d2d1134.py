def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if all:
		return [(name, getattr(self, name).description) for name in dir(self) if not name.startswith('_')]
	else:
		return [(name, getattr(self, name).description) for name in dir(self) if not name.startswith('_') and not name.startswith('__')]