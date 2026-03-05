def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="Run a command-line tool.")
	parser.add_argument("--version", action="version", version="%(prog)s 0.1")
	subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")
	subparsers.required = True
	subparsers.add_parser("global", help="global options")
	subparsers.add_parser("foo", help="foo options")
	subparsers.add_parser("bar", help="bar options")
	return parser.parse_args(unparsed_arguments)