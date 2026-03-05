def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(parents=[unparsed_arguments[0]])
	subparsers = parser.add_subparsers(dest="subparser_name")
	subparsers.add_parser("global").set_defaults(func=lambda *args: None)
	return dict(
		(subparser_name, vars(args.subparser_name))
		for subparser_name, args in vars(parser.parse_known_args(unparsed_arguments)[0]).items()
		if args.subparser_name != "global"
	)