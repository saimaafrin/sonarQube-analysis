def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	if cli_args.has_key('deprecated_args'):
		for arg in cli_args['deprecated_args']:
			if arg in answer_file_args:
				print "WARNING: Argument '%s' is deprecated. Please use '%s' instead." % (arg, cli_args['deprecated_args'][arg])