def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.VCS = 'git'
	config.style = 'pep440'
	config.tag_prefix = 'v'
	config.parentdir_prefix = '.'
	config.versionfile_source = 'VERSION'
	config.versionfile_build = 'VERSION'
	config.version_scheme = 'guess-next-dev'
	config.tag_regex = r"^(?P<prefix>{prefix})(?P<version>v?(?P<baseversion>[^\\+]*)(\\+g?(?P<gitsha>[a-z0-9]+))?)(?P<suffix>.*)$".format(prefix=re.escape(config.tag_prefix))
	config.parentdir_regex = r"^(?P<prefix>{prefix})(?P<version>v?(?P<baseversion>[^\\+]*)(\\+g?(?P<gitsha>[a-z0-9]+))?)(?P<suffix>.*)$".format(prefix=re.escape(config.parentdir_prefix))
	config.version_regex = r"^(?P<version>v?(?P<baseversion>[^\\+]*)(\\+g?(?P<gitsha>[a-z0-9]+))?)(?P<suffix>.*)$"
	config.version_scheme_regex = r"^(?P<version>v?(?P<baseversion>[^\\+]*)(\\+g?(?P<gitsha>[a-z0-9]+))?)(?P<suffix>.*)$"
	config.parentdir_regex = r"^(?P<prefix>{prefix})(?P<version>v?(?P<baseversion>[^\\+]*)(\\+g?(?P<gitsha>[a-z0-9]+))?)(?P<suffix>.*)$".format(prefix=re.escape(config.parentdir_prefix))
	config.versionfile_source_regex = r"^(?P<prefix>{prefix})(?P<version>v?(?P<baseversion>[^\\+]*)(\\+g?(?P<gitsha