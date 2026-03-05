def parse_arguments(*unparsed_arguments):
    """
    Parses parameters and returns them as dict maps
    """
    parsed_arguments = {}
    for arg in unparsed_arguments:
        if '=' in arg:
            key, value = arg.split('=', 1)
            parsed_arguments[key.strip()] = value.strip()
        else:
            parsed_arguments[arg.strip()] = None
    return parsed_arguments