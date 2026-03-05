def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    # Assuming self.parser is the parser object for the specified command
    command_parser = self.parser.get_parser(command_name)
    return command_parser.get_options()