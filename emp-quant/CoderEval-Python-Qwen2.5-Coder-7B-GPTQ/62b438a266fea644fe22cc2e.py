import argparse

def parse_arguments(*unparsed_arguments):
    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest='subcommand')

    # Define your subparsers here
    # For example:
    # subparsers.add_parser('example', help='Example subcommand')
    
    parsed_args = parser.parse_args(unparsed_arguments)

    if not hasattr(parsed_args, 'subcommand'):
        parsed_args.subcommand = 'global'

    args_dict = {parsed_args.subcommand: parsed_args}
    return args_dict