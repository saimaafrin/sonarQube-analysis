import argparse

def parse_subparser_arguments(unparsed_arguments, subparsers):
    parsed_args = {}
    remaining_args = unparsed_arguments[:]
    
    for subparser_name, parser in subparsers.items():
        # Create a new argument parser that inherits from the current one
        combined_parser = argparse.ArgumentParser(add_help=False, parents=[parser])
        
        # Parse the arguments
        namespace, remaining_args = combined_parser.parse_known_args(remaining_args)
        
        if namespace:
            parsed_args[subparser_name] = namespace
    
    return parsed_args, remaining_args