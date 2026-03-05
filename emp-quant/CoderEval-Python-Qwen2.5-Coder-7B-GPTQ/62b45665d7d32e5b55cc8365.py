def parse_arguments(*unparsed_arguments):
    parsed_args = {}
    for arg in unparsed_arguments:
        if '=' in arg:
            key, value = arg.split('=', 1)
            parsed_args[key.strip()] = value.strip()
        else:
            parsed_args[arg] = True
    return parsed_args