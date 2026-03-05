def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	if parser_name == 'main':
		if 'debug' in values_dict:
			values_dict['debug'] = bool(values_dict['debug'])
		if 'verbose' in values_dict:
			values_dict['verbose'] = bool(values_dict['verbose'])
		if 'quiet' in values_dict:
			values_dict['quiet'] = bool(values_dict['quiet'])
		if 'version' in values_dict:
			values_dict['version'] = bool(values_dict['version'])
		if 'help' in values_dict:
			values_dict['help'] = bool(values_dict['help'])
		if 'config' in values_dict:
			values_dict['config'] = str(values_dict['config'])
		if 'log_file' in values_dict:
			values_dict['log_file'] = str(values_dict['log_file'])
		if 'log_level' in values_dict:
			values_dict['log_level'] = str(values_dict['log_level'])
		if 'log_format' in values_dict:
			values_dict['log_format'] = str(values_dict['log_format'])
		if 'log_date_format' in values_dict:
			values_dict['log_date_format'] = str(values_dict['log_date_format'])
		if 'log_color' in values_dict:
			values_dict['log_color'] = bool(values_dict['log_color'])
		if 'log_no_color' in values_dict:
			values_dict['log_no_color'] = bool(values_dict['log_no_color'])
		if 'log_no_date' in values_dict:
			values_dict['log_no_date'] = bool(values_dict['log_no_date'])
		if 'log_no_level' in values_dict:
			values_dict['log_no_level'] = bool(values_