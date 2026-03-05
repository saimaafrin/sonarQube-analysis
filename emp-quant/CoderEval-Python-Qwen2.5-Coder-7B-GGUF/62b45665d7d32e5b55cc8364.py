def parse_subparser_arguments(unparsed_arguments, subparsers):
    parsed_args = {}
    remaining_args = unparsed_arguments[:]
    
    for subparser_name, parser in subparsers.items():
        subparser_args = parser.parse_known_args(remaining_args)
        parsed_args[subparser_name] = subparser_args[0]
        remaining_args = subparser_args[1]
    
    return parsed_args, remaining_args