import argparse

def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict with arguments
    """
    arg_parser = getattr(self, f'_{parser_name}_arg_parser')
    for action in arg_parser._actions:
        if action.dest in values_dict:
            if isinstance(action.type, type):
                values_dict[action.dest] = action.type(values_dict[action.dest])