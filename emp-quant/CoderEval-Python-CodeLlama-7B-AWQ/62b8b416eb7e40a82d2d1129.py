def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if all:
		return self.__dict__.keys()
	else:
		return self.__dict__.keys() - self.__class__.__dict__.keys()