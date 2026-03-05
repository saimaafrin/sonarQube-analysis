def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if all:
		return [(name, getattr(self, name).description) for name in dir(self) if name[0] != '_' and name != 'namesAndDescriptions']
	else:
		return [(name, getattr(self, name).description) for name in dir(self) if name[0] != '_' and name != 'namesAndDescriptions' and not name.endswith('_')]