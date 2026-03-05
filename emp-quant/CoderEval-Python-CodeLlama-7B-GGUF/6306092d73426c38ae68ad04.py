def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	parser_option_specs = []
	for option in self.get_command_options(command_name):
		parser_option_specs.append(option.get_parser_option_spec())
	return parser_option_specs