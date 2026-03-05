def get_option_spec(self, command_name, argument_name):
	"""
	Gets the specification for the specified option name. Get options of the given command_name with self.get_parser_option_specs()
	"""
	for option_spec in self.get_parser_option_specs(command_name):
		if option_spec.name == argument_name:
			return option_spec
	return None