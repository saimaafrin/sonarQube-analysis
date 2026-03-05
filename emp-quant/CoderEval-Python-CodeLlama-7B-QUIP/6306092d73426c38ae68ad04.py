def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	parser_option_specs = []
	for option in self.parser.option_list:
		if option.get_name() == command_name:
			parser_option_specs.append(option)
	return parser_option_specs