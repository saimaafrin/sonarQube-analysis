def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc is not None:
		return explicit_mc
	if len(bases) == 0:
		return type
	if len(bases) == 1:
		return bases[0].__class__
	return bases[0].__class__