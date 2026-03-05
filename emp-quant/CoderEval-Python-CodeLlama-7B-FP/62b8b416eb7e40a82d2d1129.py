def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if all:
		return self.__dict__.keys()
	else:
		return [k for k in self.__dict__.keys() if not k.startswith('_')]