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
		if '--help-all' in values_dict:
			values_dict['--help-all'] = True
		if '--help-syntax' in values_dict:
			values_dict['--help-syntax'] = True
		if '--help-commands' in values_dict:
			values_dict['--help-commands'] = True
		if '--help-options' in values_dict:
			values_dict['--help-options'] = True
		if '--help-options-all' in values_dict:
			values_dict['--help-options-all'] = True
		if '--help-options-common' in values_dict:
			values_dict['--help-options-common'] = True
		if '--help-options-virsh' in values_dict:
			values_dict['--help-options-virsh'] = True
		if '--help-options-ospd' in values_dict:
			values_dict['--help-options-ospd'] = True
		if '--help-options-ospd-all' in values_dict:
			values_dict['--help-options-ospd-all'] = True
		if '--help-options-ospd-common' in values_dict:
			values_dict['--help-options-ospd-common'] = True
		if '--help-options-ospd-virsh' in values_dict:
			values_dict['--help-options-ospd-virsh'] = True
		if '--help-options-ospd-virsh-all' in values_dict:
			values_dict['--help-options-ospd-virsh-all'] = True
		if '--help-options-ospd-virsh-common' in values_dict: