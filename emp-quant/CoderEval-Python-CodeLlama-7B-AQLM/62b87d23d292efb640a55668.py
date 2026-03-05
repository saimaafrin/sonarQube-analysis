def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.VCS = 'git'
	config.style = 'pep440'
	config.tag_prefix = 'v'
	config.parentdir_prefix = '.'
	config.versionfile_source = 'setup.py'
	config.versionfile_build = 'setup.py'
	config.tag_regex = r"^(?P<prefix>{tag_prefix})(?P<version>[^\+]+)(?P<suffix>.*)?$".format(tag_prefix=config.tag_prefix)
	config.parentdir_regex = r"^(?P<prefix>{parentdir_prefix})(?P<version>[^\+]+)(?P<suffix>.*)?$".format(parentdir_prefix=config.parentdir_prefix)
	config.version_scheme = "guess-next-dev"
	config.local_scheme = "node-and-date"
	config.version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]$"
	config.verbose = False
	config.version_variable = "__version__"
	config.style = "pep440"
	config.versionfile_source = "setup.py"
	config.versionfile_build = "setup.py"
	config.tag_prefix = "v"
	config.parentdir_prefix = "."
	config.tag_regex = r"^(?P<prefix>{tag_prefix})(?P<version>[^\+]+)(?P<suffix>.*)?$".format(tag_prefix=config.tag_prefix)
	config.parentdir_regex = r"^(?P<prefix>{parentdir_prefix})(?P<version>[^\+]+)(?P<suffix>.*)?$".format(parentdir_prefix=config.parentdir_prefix)
	config.version_scheme = "guess-next-dev"
	config.local_scheme = "node-and-date"
	config.version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]$"
	config.verbose = False
	config.