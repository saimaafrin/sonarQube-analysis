import re

def parse_arguments(*unparsed_arguments):
    """
    Parses parameters and returns them as dict maps
    """
    parsed_args = {}
    for arg in unparsed_arguments:
        if isinstance(arg, str) and '=' in arg:
            key, value = arg.split('=', 1)
            parsed_args[key.strip()] = value.strip()
        elif isinstance(arg, dict):
            parsed_args.update(arg)
    return parsed_args