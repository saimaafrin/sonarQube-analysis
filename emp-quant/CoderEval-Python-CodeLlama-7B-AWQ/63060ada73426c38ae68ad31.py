def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	if parser_name == 'main':
		if '--version' in values_dict:
			values_dict['--version'] = True
		if '--help' in values_dict:
			values_dict['--help'] = True
		if '--debug' in values_dict:
			values_dict['--debug'] = True
		if '--verbose' in values_dict:
			values_dict['--verbose'] = True
		if '--quiet' in values_dict:
			values_dict['--quiet'] = True
		if '--no-color' in values_dict:
			values_dict['--no-color'] = True
		if '--no-warnings' in values_dict:
			values_dict['--no-warnings'] = True
		if '--no-confirm' in values_dict:
			values_dict['--no-confirm'] = True
		if '--no-prompt' in values_dict:
			values_dict['--no-prompt'] = True
		if '--no-interaction' in values_dict:
			values_dict['--no-interaction'] = True
		if '--no-progress' in values_dict:
			values_dict['--no-progress'] = True
		if '--no-spinner' in values_dict:
			values_dict['--no-spinner'] = True
		if '--no-cache' in values_dict:
			values_dict['--no-cache'] = True
		if '--no-cache-dir' in values_dict:
			values_dict['--no-cache-dir'] = True
		if '--no-cache-ttl' in values_dict:
			values_dict['--no-cache-ttl'] = True
		if '--no-cache-max-age' in values_dict:
			values_dict['--no-cache-max-age'] = True
		if '--no-cache-max-size'