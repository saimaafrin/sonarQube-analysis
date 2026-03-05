def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	size = size.upper()
	if size[-1] in ['B', 'K', 'M', 'G', 'T', 'P']:
		size = size[:-1]
	size = float(size)
	if size[-1] == 'B':
		return int(size)
	if size[-1] == 'K':
		return int(size * 1024)
	if size[-1] == 'M':
		return int(size * 1024 * 1024)
	if size[-1] == 'G':
		return int(size * 1024 * 1024 * 1024)
	if size[-1] == 'T':
		return int(size * 1024 * 1024 * 1024 * 1024)
	if size[-1] == 'P':
		return int(size * 1024 * 1024 * 1024 * 1024 * 1024)
	return int(size)