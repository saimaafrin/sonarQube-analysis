import argparse

def parse_arguments(*unparsed_arguments):
    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest='subparser_name', required=True)

    # Define your subparsers here
    # For example:
    # subparsers.add_parser('subparser1')
    # subparsers.add_parser('subparser2')

    parsed_args = parser.parse_args(unparsed_arguments)
    return {parsed_args.subparser_name: parsed_args}