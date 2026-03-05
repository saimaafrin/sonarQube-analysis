def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	size = size.lower()
	if size[-1] == 'b':
		return int(size[:-1])
	if size[-2:] == 'kb':
		return int(size[:-2]) * 1024
	if size[-2:] == 'mb':
		return int(size[:-2]) * 1024 * 1024
	if size[-2:] == 'gb':
		return int(size[:-2]) * 1024 * 1024 * 1024
	if size[-2:] == 'tb':
		return int(size[:-2]) * 1024 * 1024 * 1024 * 1024
	if size[-2:] == 'pb':
		return int(size[:-2]) * 1024 * 1024 * 1024 * 1024 * 1024
	if size[-2:] == 'eb':
		return int(size[:-2]) * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
	if size[-2:] == 'zb':
		return int(size[:-2]) * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
	if size[-2:] == 'yb':
		return int(size[:-2]) * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
	raise ValueError('Invalid size')