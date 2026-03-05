import argparse

def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    argparser = getattr(self, f'_{parser_name}_argparser')
    for action in argparser._actions:
        if isinstance(action, argparse.Action) and action.dest in values_dict:
            value = values_dict[action.dest]
            try:
                if action.nargs == argparse.OPTIONAL:
                    values_dict[action.dest] = type(action.default)(value)
                else:
                    values_dict[action.dest] = [type(action.choices[0])(v) for v in value.split()]
            except ValueError:
                raise ValueError(f"Invalid value for {action.dest}: {value}")