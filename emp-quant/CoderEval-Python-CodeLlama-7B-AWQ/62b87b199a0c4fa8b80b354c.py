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
	elif isinstance(seq, buffer):
		return seq, buffer
	elif isinstance(seq, array.array):
		return seq, array.array
	elif isinstance(seq, array.array_type):
		return seq, array.array_type
	elif isinstance(seq, array.array_types):
		return seq, array.array_types
	elif isinstance(seq, array.typecode_type):
		return seq, array.typecode_type
	elif isinstance(seq, array.typecode_types):
		return seq, array.typecode_types
	elif isinstance(seq, array.type_type):
		return seq, array.type_type
	elif isinstance(seq, array.type_types):
		return seq, array.type_types
	elif isinstance(seq, array.chararray):
		return seq, array.chararray
	elif isinstance(seq, array.c_chararray):
		return seq, array.c_chararray
	elif isinstance(seq, array.c_wchararray):
		return seq, array.c_wchararray
	elif isinstance(seq, array.c_void_p):
		return seq, array.c_void_p
	elif isinstance(seq, array.c_int):
		return seq, array.c_int
	elif isinstance(seq, array.c_long):
		return seq, array.c_long
	elif isinstance(seq, array.c_longlong):
		return seq, array.c_longlong
	elif isinstance(seq, array.c_size_t):
		return seq, array.c_size_t
	elif isinstance(seq, array.c_ss