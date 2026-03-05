def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if output is None:
		output = []
	for item in sequence:
		if isinstance(item, Declaration):
			output.append(item)
		elif isinstance(item, tuple):
			output.append(item)
		elif isinstance(item, Interface):
			output.append(item)
		else:
			for subitem in item:
				if isinstance(subitem, Declaration):
					output.append(subitem)
				elif isinstance(subitem, tuple):
					output.append(subitem)
				elif isinstance(subitem, Interface):
					output.append(subitem)
				else:
					raise TypeError("Invalid item in declaration sequence: %r" % (subitem,))
	return output