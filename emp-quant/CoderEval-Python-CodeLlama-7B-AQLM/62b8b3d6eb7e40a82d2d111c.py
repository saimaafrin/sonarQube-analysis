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
		return sequence
	elif isinstance(sequence, list):
		return tuple(sequence)
	elif isinstance(sequence, str):
		return (sequence,)
	elif isinstance(sequence, Interface):
		return (sequence,)
	elif isinstance(sequence, Implements):
		return (sequence,)
	elif isinstance(sequence, ImplementsSpec):
		return (sequence,)
	elif isinstance(sequence, ImplementsSpecList):
		return sequence
	elif isinstance(sequence, ImplementsSpecTuple):
		return sequence
	elif isinstance(sequence, ImplementsSpecSequence):
		return sequence
	elif isinstance(sequence, ImplementsSpecSet):
		return sequence
	elif isinstance(sequence, ImplementsSpecList):
		return sequence
	elif isinstance(sequence, ImplementsSpecTuple):
		return sequence
	elif isinstance(sequence, ImplementsSpecSequence):
		return sequence
	elif isinstance(sequence, ImplementsSpecSet):
		return sequence
	elif isinstance(sequence, ImplementsSpecList):
		return sequence
	elif isinstance(sequence, ImplementsSpecTuple):
		return sequence
	elif isinstance(sequence, ImplementsSpecSequence):
		return sequence
	elif isinstance(sequence, ImplementsSpecSet):
		return sequence
	elif isinstance(sequence, ImplementsSpecList):
		return sequence
	elif isinstance(sequence, ImplementsSpecTuple):
		return sequence
	elif isinstance(sequence, ImplementsSpecSequence):
		return sequence
	elif isinstance(sequence, ImplementsSpecSet):
		return sequence
	elif isinstance(sequence, ImplementsSpecList):
		return sequence
	elif isinstance(sequence, ImplementsSpecTuple):
		return sequence
	elif isinstance(sequence, ImplementsSpecSequence):
		return sequence
	elif isinstance(sequence, ImplementsSpecSet):
		return sequence
	elif isinstance(sequence, ImplementsSpecList):
		return sequence
	elif isinstance(sequence