def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	return set(cls.__subclasses__())