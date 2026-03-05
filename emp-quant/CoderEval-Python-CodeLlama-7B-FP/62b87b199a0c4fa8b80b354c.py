def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if bufsize is None:
		bufsize = len(seq)
	if isinstance(seq, (str, bytes)):
		return seq, type(seq)
	elif isinstance(seq, (list, tuple)):
		return seq, type(seq)
	elif isinstance(seq, (bytearray, memoryview)):
		return seq, type(seq)
	elif isinstance(seq, (array.array,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (array.array,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif isinstance(seq, (buffer,)):
		return seq, type(seq)
	elif