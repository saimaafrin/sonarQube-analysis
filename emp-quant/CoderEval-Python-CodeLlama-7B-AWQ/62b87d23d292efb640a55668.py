def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.VCS = 'git'
	config.style = 'pep440'
	config.tag_prefix = 'v'
	config.parentdir_prefix = '.'
	config.parentdir_prefix_strip = 0
	config.versionfile_source = 'src/version.py'
	config.verbose = True
	config.version_scheme = lambda v: v.strip('v')
	config.versionfile_build = 'src/version.py'
	config.key = 'version'
	config.version_variable = 'version'
	config.parentdir_build = '.'
	config.style = 'pep440'
	config.version_scheme = lambda v: v.strip('v')
	config.verbose = True
	return config