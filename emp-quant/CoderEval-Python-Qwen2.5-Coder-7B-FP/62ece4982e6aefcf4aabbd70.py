def os_is_mac():
# Importing platform module
	import platform
	
	# Getting OS name
	os_name = platform.system()
	
	# Checking if OS is macOS
	return os_name == 'Darwin'