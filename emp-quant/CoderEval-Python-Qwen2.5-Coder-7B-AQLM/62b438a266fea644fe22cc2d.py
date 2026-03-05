def parse_subparser_arguments(unparsed_arguments, subparsers):
    parsed_args = {}
    remaining_args = unparsed_arguments[:]
    
    for subparser_name, subparser in subparsers.items():
        parser = subparser.parse_known_args(remaining_args)
        parsed_args[subparser_name] = parser[0]
        remaining_args = parser[1]
    
    return parsed_args, remaining_args