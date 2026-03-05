def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="Run a command on a remote machine.")
	parser.add_argument("--version", action="version", version="%(prog)s " + __version__)
	subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")
	subparsers.required = True
	subparsers.add_parser("global", help="global options")
	subparsers.add_parser("ssh", help="ssh options")
	subparsers.add_parser("scp", help="scp options")
	subparsers.add_parser("sftp", help="sftp options")
	subparsers.add_parser("rsync", help="rsync options")
	subparsers.add_parser("ssh-agent", help="ssh-agent options")
	subparsers.add_parser("ssh-keygen", help="ssh-keygen options")
	subparsers.add_parser("ssh-keyscan", help="ssh-keyscan options")
	subparsers.add_parser("ssh-keysign", help="ssh-keysign options")
	subparsers.add_parser("ssh-add", help="ssh-add options")
	subparsers.add_parser("ssh-copy-id", help="ssh-copy-id options")
	subparsers.add_parser("ssh-keygen", help="ssh-keygen options")
	subparsers.add_parser("ssh-keyscan", help="ssh-keyscan options")
	subparsers.add_parser("ssh-keysign", help="ssh-keysign options")
	subparsers.add_parser("ssh-add", help="ssh-add options")
	subparsers.add_parser("ssh-copy-id", help="ssh-copy-id options")
	subparsers.add_parser("ssh-keygen", help="ssh-keygen options")
	subparsers.add_parser("ssh-keyscan", help="ssh-keyscan options")
	subparsers.add_parser("ssh-keysign", help="ssh-keysign options")
	subparsers.add_parser("ssh-add", help="ssh-add options")