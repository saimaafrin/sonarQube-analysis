def unit_of_work(metadata=None, timeout=None):
	"""
	Returns a decorator with metadata and timeout attributes.
	"""
	return {
		"metadata": metadata,
		"timeout": timeout
	}