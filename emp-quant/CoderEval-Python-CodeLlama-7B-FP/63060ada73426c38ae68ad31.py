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
		if '--log-file' in values_dict:
			values_dict['--log-file'] = values_dict['--log-file']
		if '--log-level' in values_dict:
			values_dict['--log-level'] = values_dict['--log-level']
		if '--log-format' in values_dict:
			values_dict['--log-format'] = values_dict['--log-format']
		if '--log-date-format' in values_dict:
			values_dict['--log-date-format'] = values_dict['--log-date-format']
		if '--log-file-size' in values_dict:
			values_dict['--log-file-size'] = values_dict['--log-file-size']
		if '--log-file-count' in values_dict:
			values_dict['--log-file-count'] = values_dict['--log-file-count']
		if '--log-file-backup-count' in values_dict:
			values_dict['--log-file-backup-count'] = values_dict['--log-file-backup-count']
		if '--log-file-max-age' in values_dict:
			values_dict['--log-file-max-age'] = values_dict['--log-file-max-age']
		if '--log-file-max-backups' in values_dict:
			values_dict['--log-file-max-backups'] = values_dict['--log-file-max-backups']
		if '--log-file-max-size' in values_dict:
			values