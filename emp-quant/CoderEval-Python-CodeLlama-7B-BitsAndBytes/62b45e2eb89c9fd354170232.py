def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	parts = version.split('.')
	parts[-1] = str(int(parts[-1]) + 1)
	return '.'.join(parts)