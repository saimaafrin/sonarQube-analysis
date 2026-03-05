def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	subclasses = set()
	for subclass in cls.__subclasses__():
		subclasses.add(subclass)
		subclasses.update(subclasses_of(subclass))
	return subclasses