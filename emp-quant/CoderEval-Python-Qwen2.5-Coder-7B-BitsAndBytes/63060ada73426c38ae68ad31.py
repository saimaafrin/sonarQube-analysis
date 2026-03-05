import argparse

def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    parser = self._get_parser(parser_name)
    for arg, value in values_dict.items():
        if arg in parser._actions:
            action = parser._actions[parser._actions.index(next(a for a in parser._actions if a.dest == arg))]
            if action.nargs == argparse.OPTIONAL and value is None:
                continue
            try:
                converted_value = action.type(value)
                values_dict[arg] = converted_value
            except (ValueError, TypeError):
                pass