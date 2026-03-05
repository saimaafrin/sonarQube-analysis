def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    # Define type mappings for different parsers
    type_mappings = {
        'main': {
            'int_arg': int,
            'float_arg': float,
            'bool_arg': bool,
        },
        'virsh': {
            'domain_id': int,
            'timeout': int,
        },
        'ospd': {
            'port': int,
            'debug': bool,
        },
    }

    # Get the type mapping for the given parser
    parser_types = type_mappings.get(parser_name, {})

    # Iterate over the values_dict and cast the values to the correct types
    for key, value in values_dict.items():
        if key in parser_types:
            values_dict[key] = parser_types[key](value)