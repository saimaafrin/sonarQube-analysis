def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, str):
		seq = seq.encode()
	if isinstance(seq, bytes):
		return seq, 'bytes'
	if isinstance(seq, bytearray):
		return seq, 'bytearray'
	if isinstance(seq, memoryview):
		return seq, 'memoryview'
	if isinstance(seq, array.array):
		return seq, 'array'
	if isinstance(seq, list):
		return seq, 'list'
	if isinstance(seq, tuple):
		return seq, 'tuple'
	if isinstance(seq, range):
		return seq, 'range'
	if isinstance(seq, set):
		return seq, 'set'
	if isinstance(seq, frozenset):
		return seq, 'frozenset'
	if isinstance(seq, dict):
		return seq, 'dict'
	if isinstance(seq, collections.abc.Sequence):
		return seq, 'Sequence'
	if isinstance(seq, collections.abc.MutableSequence):
		return seq, 'MutableSequence'
	if isinstance(seq, collections.abc.Iterable):
		return seq, 'Iterable'
	if isinstance(seq, collections.abc.Iterator):
		return seq, 'Iterator'
	if isinstance(seq, collections.abc.Reversible):
		return seq, 'Reversible'
	if isinstance(seq, collections.abc.Container):
		return seq, 'Container'
	if isinstance(seq, collections.abc.Sized):
		return seq, 'Sized'
	if isinstance(seq, collections.abc.Hashable):
		return seq, 'Hashable'
	if isinstance(seq, collections.abc.Callable):
		return seq, 'Callable'
	if isinstance(seq, collections.abc.ContextManager):
		return seq, 'ContextManager'
	if isinstance(seq, collections.abc.Awaitable):
		return seq, 'Awaitable'
	if isinstance(seq, collections.abc.AsyncIterable):
		return