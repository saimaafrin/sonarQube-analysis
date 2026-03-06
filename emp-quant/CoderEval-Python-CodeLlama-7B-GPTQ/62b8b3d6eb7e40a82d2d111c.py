def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if isinstance(sequence, Declaration):
		return sequence
	elif isinstance(sequence, tuple):
		return tuple(_normalizeargs(x, output) for x in sequence)
	elif isinstance(sequence, list):
		return [_normalizeargs(x, output) for x in sequence]
	elif isinstance(sequence, Interface):
		return sequence
	elif isinstance(sequence, Implements):
		return sequence
	elif isinstance(sequence, str):
		return sequence
	elif isinstance(sequence, (int, float)):
		return sequence
	elif isinstance(sequence, (list, tuple)):
		return tuple(sequence)
	else:
		raise TypeError(f"Unknown type {type(sequence)}")