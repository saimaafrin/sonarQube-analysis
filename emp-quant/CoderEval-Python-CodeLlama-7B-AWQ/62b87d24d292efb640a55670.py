def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		return get_versions_from_file()
	except:
		return get_versions_from_default()