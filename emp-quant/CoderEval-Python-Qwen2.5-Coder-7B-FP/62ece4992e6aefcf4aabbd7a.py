def is_gitbash():
# Check if the 'SHELL' environment variable is set to '/bin/bash'
	return os.environ.get('SHELL', '') == '/bin/bash'