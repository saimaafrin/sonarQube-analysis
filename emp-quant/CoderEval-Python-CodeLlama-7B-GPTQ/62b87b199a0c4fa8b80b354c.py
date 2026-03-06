def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, (list, tuple)):
		return seq, type(seq)
	elif isinstance(seq, str):
		return seq, str
	elif isinstance(seq, bytes):
		return seq, bytes
	elif isinstance(seq, bytearray):
		return seq, bytearray
	elif isinstance(seq, memoryview):
		return seq, memoryview
	elif isinstance(seq, array.array):
		return seq, array.array
	elif isinstance(seq, array.array_type):
		return seq, array.array_type
	elif isinstance(seq, buffer):
		return seq, buffer
	elif isinstance(seq, buffer_type):
		return seq, buffer_type
	elif isinstance(seq, memoryview):
		return seq, memoryview
	elif isinstance(seq, memoryview_type):
		return seq, memoryview_type
	elif isinstance(seq, (range, xrange)):
		return seq, type(seq)
	elif isinstance(seq, (list, tuple, set, frozenset)):
		return seq, type(seq)
	elif isinstance(seq, (dict, OrderedDict)):
		return seq, type(seq)
	elif isinstance(seq, (deque, collections.deque)):
		return seq, type(seq)
	elif isinstance(seq, (collections.OrderedDict, collections.OrderedDict)):
		return seq, type(seq)
	elif isinstance(seq, (collections.Counter, collections.Counter)):
		return seq, type(seq)
	elif isinstance(seq, (collections.defaultdict, collections.defaultdict)):
		return seq, type(seq)
	elif isinstance(seq, (collections.ChainMap, collections.ChainMap)):
		return seq, type(seq)
	elif isinstance(seq, (collections.UserList, collections.UserList)):
		return seq, type(seq)
	elif isinstance(seq, (collections.UserDict, collections.UserDict)):
		return seq, type(seq)
	elif isinstance(seq, (collections.UserString