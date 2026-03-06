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
	config.versionfile_upstream = 'src/version.py'
	config.version_scheme = 'guess-next-dev'
	config.local_scheme = 'node-and-date'
	config.version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
	config.parentdir_regex = r"^__parentdir__ = ['\"]([^'\"]*)['\"]"
	config.version_cls = 'src.version'
	return config