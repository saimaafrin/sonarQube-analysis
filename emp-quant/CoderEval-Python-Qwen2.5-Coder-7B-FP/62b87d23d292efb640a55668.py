def get_config():
# create the config object
	config = VersioneerConfig()
	
	# set the version file path
	config.versionfile_source = "src/my_package/_version.py"
	
	# set the version file destination path
	config.versionfile_build = "build/lib/my_package/_version.py"
	
	# set the tag prefix
	config.tag_prefix = "v"
	
	# set the parentdir_prefix
	config.parentdir_prefix = "my_package-"
	
	# return the config object
	return config

config = get_config()

print(config)