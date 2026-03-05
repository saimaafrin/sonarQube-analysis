def parse_arguments(*unparsed_arguments):
# Import here to avoid circular import issues
	import argparse

	# Create top-level parser
	top_parser = argparse.ArgumentParser(add_help=False)
	subparsers = top_parser.add_subparsers(dest="subcommand")

	# Add global options
	global_options = subparsers.add_parser("global", add_help=False)

	# Define subcommands and their options
	for subcommand_name, subcommand_parser in unparsed_arguments:
		subcommand_parser.set_defaults(subcommand=subcommand_name)
		subparsers.add_parser(subcommand_name, parents=[top_parser], help=subcommand_parser.description)

	# Parse arguments
	args = top_parser.parse_args()

	# Group parsed arguments by subcommand
	result = {}
	if args.subcommand == "global":
		result["global"] = args
	else:
		result[args.subcommand] = args

	return result