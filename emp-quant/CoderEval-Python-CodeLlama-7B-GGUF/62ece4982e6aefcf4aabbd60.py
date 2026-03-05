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
	size = size.replace(',', '')
	size = size.replace(' ', '')
	size = size.replace('_', '')
	size = size.replace('-', '')
	size = size.replace('+', '')
	size = size.replace('=', '')
	size = size.replace('*', '')
	size = size.replace('/', '')
	size = size.replace('\\', '')
	size = size.replace('|', '')
	size = size.replace(':', '')
	size = size.replace(';', '')
	size = size.replace('"', '')
	size = size.replace("'", '')
	size = size.replace('<', '')
	size = size.replace('>', '')
	size = size.replace('?', '')
	size = size.replace('!', '')
	size = size.replace('@', '')
	size = size.replace('#', '')
	size = size.replace('$', '')
	size = size.replace('%', '')
	size = size.replace('^', '')
	size = size.replace('&', '')
	size = size.replace('*', '')
	size = size.replace('(', '')
	size = size.replace(')', '')
	size = size.replace('[', '')
	size = size.replace(']', '')
	size = size.replace('{', '')
	size = size.replace('}', '')
	size = size.replace('~', '')
	size = size.replace('`', '')
	size = size.replace(' ', '')
	size = size.replace('\t', '')
	size = size.replace('\n', '')
	size = size.replace('\r', '')
	size = size.replace('\x00', '')
	size = size.replace('\x01', '')
	size = size.replace('\x02', '')
	size = size.replace('\x03', '')
	size = size.replace('\x