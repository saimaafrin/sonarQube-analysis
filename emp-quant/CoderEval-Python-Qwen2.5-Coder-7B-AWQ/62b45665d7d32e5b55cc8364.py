import argparse

def parse_subparser_arguments(unparsed_arguments, subparsers):
    parsed_namespaces = {}
    remaining_arguments = unparsed_arguments[:]
    
    for subparser_name, parser in subparsers.items():
        args, unknown_args = parser.parse_known_args(remaining_arguments)
        if args:
            parsed_namespaces[subparser_name] = args
            remaining_arguments = unknown_args
    
    return parsed_namespaces, remaining_arguments