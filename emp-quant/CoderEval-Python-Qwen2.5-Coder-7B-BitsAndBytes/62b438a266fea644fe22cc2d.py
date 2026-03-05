import argparse

def parse_subparser_arguments(unparsed_arguments, subparsers):
    parsed_namespaces = {}
    remaining_args = unparsed_arguments[:]
    
    for subparser_name, parser in subparsers.items():
        # Create a copy of the remaining arguments to avoid modifying the original list
        args_to_parse = remaining_args[:]
        
        # Attempt to parse the arguments using the current subparser
        try:
            namespace, remaining = parser.parse_known_args(args_to_parse)
            parsed_namespaces[subparser_name] = namespace
            
            # Remove the successfully parsed arguments from the remaining list
            remaining_args = [arg for arg in remaining_args if arg not in args_to_parse]
        except SystemExit:
            # If the parser raises SystemExit, it means it couldn't parse the arguments
            continue
    
    return parsed_namespaces, remaining_args