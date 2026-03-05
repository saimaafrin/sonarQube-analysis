def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).
	"""
	# The first argument is the subparser name.
	subparser_name = unparsed_arguments[0]
	subparser = subparsers[subparser_name]
	subparser_arguments = unparsed_arguments[1:]
	subparser_namespace = subparser.parse_args(subparser_arguments)
	return (subparser_name, subparser_namespace, subparser_arguments)