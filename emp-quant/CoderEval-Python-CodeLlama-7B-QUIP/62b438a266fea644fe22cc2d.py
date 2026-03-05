def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).
	"""
	parsed_arguments = {}
	unparsed_arguments = unparsed_arguments[:]
	for subparser_name, subparser in subparsers.items():
		try:
			parsed_arguments[subparser_name] = subparser.parse_args(unparsed_arguments)
			unparsed_arguments = unparsed_arguments[1:]
		except argparse.ArgumentError as e:
			if e.code == argparse.ArgumentError.CODE_UNKNOWN_SUBPARSER:
				raise e
			else:
				raise e
	return parsed_arguments, unparsed_arguments