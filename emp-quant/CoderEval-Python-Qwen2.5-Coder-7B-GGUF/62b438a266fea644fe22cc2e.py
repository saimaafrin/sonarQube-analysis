import argparse

def parse_arguments(*unparsed_arguments):
    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest='subparser_name')
    
    # Add subparsers here
    # Example:
    # subparsers.add_parser('subparser1')
    # subparsers.add_parser('subparser2')
    
    args = parser.parse_args(unparsed_arguments)
    return {args.subparser_name: args} if args.subparser_name else {'global': args}