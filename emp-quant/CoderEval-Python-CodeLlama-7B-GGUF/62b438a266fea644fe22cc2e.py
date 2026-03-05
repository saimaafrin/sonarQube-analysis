def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="A tool for generating and managing a local copy of a git repository.")
	parser.add_argument("--version", action="version", version="%(prog)s " + __version__)
	subparsers = parser.add_subparsers(dest="subparser_name")
	subparsers.required = True
	subparsers.add_parser("global", help="Global options")
	subparsers.add_parser("init", help="Initialize a new local copy of a git repository")
	subparsers.add_parser("pull", help="Pull changes from the remote repository")
	subparsers.add_parser("push", help="Push changes to the remote repository")
	subparsers.add_parser("status", help="Show the status of the local copy of the repository")
	subparsers.add_parser("update", help="Update the local copy of the repository to the latest version")
	subparsers.add_parser("version", help="Show the version of this tool")
	return {
		subparser_name: parser.parse_args(unparsed_arguments)
		for subparser_name, parser in subparsers.choices.items()
	}