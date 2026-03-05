import argparse

def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    parser = argparse.ArgumentParser(description='Parse command-line arguments')
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Add subparsers here
    # subparser = subparsers.add_parser('subcommand_name', help='description')
    # subparser.add_argument('--arg', help='description')

    parsed_args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to hold the results
    results = {}

    # Add the global arguments
    results['global'] = parsed_args

    # Add the subcommand arguments
    if parsed_args.subparser_name:
        results[parsed_args.subparser_name] = parsed_args

    return results