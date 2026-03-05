def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc:
		return explicit_mc
	else:
		for base in bases:
			if hasattr(base, '__metaclass__'):
				return base.__metaclass__
		return type