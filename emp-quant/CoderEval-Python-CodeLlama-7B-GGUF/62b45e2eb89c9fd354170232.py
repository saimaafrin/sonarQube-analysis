def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	version_parts = version.split('.')
	version_parts[-1] = str(int(version_parts[-1]) + 1)
	return '.'.join(version_parts)