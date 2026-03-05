def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if all:
		return self.attrs.keys()
	else:
		return [attr for attr in self.attrs if attr.name != '__init__']