def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).
	"""
	parsed_arguments = {}
	unparsed_arguments = list(unparsed_arguments)
	while unparsed_arguments:
		argument = unparsed_arguments.pop(0)
		if argument in subparsers:
			parsed_arguments[argument] = subparsers[argument].parse_args(unparsed_arguments)
			break
		else:
			unparsed_arguments.insert(0, argument)
	return parsed_arguments, unparsed_arguments