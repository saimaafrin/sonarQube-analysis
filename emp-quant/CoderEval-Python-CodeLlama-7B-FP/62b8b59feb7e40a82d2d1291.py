def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	return 'Py' + self.__class__.__name__