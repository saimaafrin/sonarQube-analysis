def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="A tool for generating a random password.")
	subparsers = parser.add_subparsers(dest="subparser_name")
	subparsers.required = True

	global_parser = subparsers.add_parser("global", help="Global options")
	global_parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")

	generate_parser = subparsers.add_parser("generate", help="Generate a password")
	generate_parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password")
	generate_parser.add_argument("-c", "--characters", type=str, default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", help="Characters to use in the password")
	generate_parser.add_argument("-n", "--no-symbols", action="store_true", help="Do not include symbols in the password")
	generate_parser.add_argument("-s", "--symbols", type=str, default="!@#$%^&*()_+-=[]{}|;:,./<>?", help="Symbols to use in the password")
	generate_parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase characters in the password")
	generate_parser.add_argument("-lc", "--lowercase", action="store_true", help="Include lowercase characters in the password")
	generate_parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers in the password")

	args = parser.parse_args(unparsed_arguments)
	return args