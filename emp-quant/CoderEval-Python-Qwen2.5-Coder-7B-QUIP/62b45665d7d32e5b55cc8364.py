import argparse

def parse_subparser_arguments(unparsed_arguments, subparsers):
    parsed_args = {}
    remaining_args = []

    for arg in unparsed_arguments:
        for subparser_name, subparser in subparsers.items():
            try:
                namespace = subparser.parse_known_args([arg])[0]
                if namespace:
                    parsed_args[subparser_name] = namespace
                    break
            except argparse.ArgumentError:
                pass

    remaining_args = [arg for arg in unparsed_arguments if arg not in parsed_args.values()]

    return parsed_args, remaining_args