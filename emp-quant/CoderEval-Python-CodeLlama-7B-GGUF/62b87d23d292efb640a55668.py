def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.VCS = 'git'
	config.style = 'pep440'
	config.tag_prefix = 'v'
	config.parentdir_prefix = '.'
	config.versionfile_source = 'src/version.py'
	config.versionfile_build = 'src/version.py'
	config.version_variable = '__version__'
	config.version_format = '{tag}.dev{commitcount}+{gitsha}'
	config.parentdir_prefix = '.'
	config.version_scheme = 'guess-next-dev'
	config.verbose = 0
	config.warn_dirty = 0
	config.style = 'pep440'
	config.tag_prefix = 'v'
	config.parentdir_prefix = '.'
	config.versionfile_source = 'src/version.py'
	config.versionfile_build = 'src/version.py'
	config.version_variable = '__version__'
	config.version_format = '{tag}.dev{commitcount}+{gitsha}'
	config.parentdir_prefix = '.'
	config.version_scheme = 'guess-next-dev'
	config.verbose = 0
	config.warn_dirty = 0
	return config