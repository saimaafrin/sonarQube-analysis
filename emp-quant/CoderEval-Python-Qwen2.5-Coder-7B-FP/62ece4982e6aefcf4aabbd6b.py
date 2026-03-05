def subclasses(cls):
# Get all direct subclasses
	subclasses = cls.__subclasses__()
	
	# Recursively get all subclasses of each subclass
	for subclass in subclasses:
		subclasses += subclasses(subclass)
	
	return subclasses