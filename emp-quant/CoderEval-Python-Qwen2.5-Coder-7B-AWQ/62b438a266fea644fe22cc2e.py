import argparse

def parse_arguments(*unparsed_arguments):
    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Add your subparsers here
    # Example:
    # subparser1 = subparsers.add_parser('subparser1')
    # subparser1.add_argument('--option1', type=str)

    args = parser.parse_args(unparsed_arguments)
    if args.subparser_name is None:
        args.subparser_name = 'global'

    return {args.subparser_name: args}