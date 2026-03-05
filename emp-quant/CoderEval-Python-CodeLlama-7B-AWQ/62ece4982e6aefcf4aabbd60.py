def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	if size[-1] in ['K', 'M', 'G', 'T', 'P']:
		size = float(size[:-1])
	else:
		size = float(size)
	if size[-1] == 'K':
		size *= 1024
	elif size[-1] == 'M':
		size *= 1024 * 1024
	elif size[-1] == 'G':
		size *= 1024 * 1024 * 1024
	elif size[-1] == 'T':
		size *= 1024 * 1024 * 1024 * 1024
	elif size[-1] == 'P':
		size *= 1024 * 1024 * 1024 * 1024 * 1024
	return int(size)