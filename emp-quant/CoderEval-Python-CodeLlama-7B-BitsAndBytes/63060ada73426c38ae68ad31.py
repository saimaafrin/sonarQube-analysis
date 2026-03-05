def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	if parser_name == 'main':
		if '--debug' in values_dict:
			values_dict['--debug'] = True
		if '--log-file' in values_dict:
			values_dict['--log-file'] = values_dict['--log-file']
		if '--log-level' in values_dict:
			values_dict['--log-level'] = values_dict['--log-level']
		if '--log-format' in values_dict:
			values_dict['--log-format'] = values_dict['--log-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-date-format'