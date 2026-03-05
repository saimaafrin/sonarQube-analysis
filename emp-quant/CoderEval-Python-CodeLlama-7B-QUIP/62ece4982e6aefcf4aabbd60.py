def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	if size.endswith('b'):
		size = size[:-1]
	if size.endswith('B'):
		size = size[:-1]
	if size.endswith('k'):
		size = size[:-1]
	if size.endswith('K'):
		size = size[:-1]
	if size.endswith('m'):
		size = size[:-1]
	if size.endswith('M'):
		size = size[:-1]
	if size.endswith('g'):
		size = size[:-1]
	if size.endswith('G'):
		size = size[:-1]
	if size.endswith('t'):
		size = size[:-1]
	if size.endswith('T'):
		size = size[:-1]
	if size.endswith('p'):
		size = size[:-1]
	if size.endswith('P'):
		size = size[:-1]
	if size.endswith('e'):
		size = size[:-1]
	if size.endswith('E'):
		size = size[:-1]
	if size.endswith('f'):
		size = size[:-1]
	if size.endswith('F'):
		size = size[:-1]
	if size.endswith('a'):
		size = size[:-1]
	if size.endswith('A'):
		size = size[:-1]
	if size.endswith('o'):
		size = size[:-1]
	if size.endswith('O'):
		size = size[:-1]
	if size.endswith('n'):
		size = size[:-1]
	if size.endswith('N'):
		size = size[:-1]
	if size.endswith('d'):
		size = size[:-1]
	if size.endswith('D'):
		size = size[:-1]
	if size.endswith('s'):
		size = size[:-1]
	if size.endswith('S'):
		size