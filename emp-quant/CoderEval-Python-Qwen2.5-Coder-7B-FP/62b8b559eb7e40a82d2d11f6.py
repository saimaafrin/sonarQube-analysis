def determineMetaclass(bases, explicit_mc=None):
# If an explicit metaclass is provided, use it
	if explicit_mc:
		return explicit_mc

	# Determine the metaclass by checking the first base class
	for base in bases:
		if hasattr(base, '__class__'):
			return type(base)

	# If no metaclass is found, default to 'type'
	return type