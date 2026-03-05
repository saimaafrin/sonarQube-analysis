import argparse

def parse_arguments(*unparsed_arguments):
    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest='subcommand')

    # Add your subparsers here
    # Example:
    # subparser1 = subparsers.add_parser('subcommand1', help='Help for subcommand1')
    # subparser1.add_argument('--option1', help='Option 1 for subcommand1')

    args = parser.parse_args(unparsed_arguments)

    result = {'global': args}
    if args.subcommand:
        result[args.subcommand] = vars(getattr(args, args.subcommand))

    return result