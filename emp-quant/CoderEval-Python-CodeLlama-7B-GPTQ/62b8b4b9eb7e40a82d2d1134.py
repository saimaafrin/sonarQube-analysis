def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if all:
		return self.namesAndDescriptions()
	else:
		return self.namesAndDescriptions(all=False)