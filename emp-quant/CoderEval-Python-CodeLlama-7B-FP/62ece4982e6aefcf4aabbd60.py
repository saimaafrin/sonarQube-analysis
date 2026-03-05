def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	size = size.upper()
	if size[-1] in ['B', 'K', 'M', 'G', 'T']:
		size = size[:-1]
	else:
		size = size
	size = float(size)
	if size[-1] == 'K':
		size = size * 1024
	elif size[-1] == 'M':
		size = size * 1024 * 1024
	elif size[-1] == 'G':
		size = size * 1024 * 1024 * 1024
	elif size[-1] == 'T':
		size = size * 1024 * 1024 * 1024 * 1024
	else:
		size = size
	return int(size)