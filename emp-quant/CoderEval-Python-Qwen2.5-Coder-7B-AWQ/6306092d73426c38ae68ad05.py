def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name. Get options of the given command_name with self.get_parser_option_specs()
    """
    parser_option_specs = self.get_parser_option_specs(command_name)
    return next((spec for spec in parser_option_specs if spec['name'] == argument_name), None)