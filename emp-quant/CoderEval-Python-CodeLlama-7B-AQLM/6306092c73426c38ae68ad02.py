def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	if cli_args.get('deprecated_args'):
		for arg in cli_args['deprecated_args']:
			print("Warning: The argument '{}' is deprecated. Please use '{}' instead.".format(arg, cli_args['deprecated_args'][arg]))

	if answer_file_args.get('deprecated_args'):
		for arg in answer_file_args['deprecated_args']:
			print("Warning: The argument '{}' is deprecated. Please use '{}' instead.".format(arg, answer_file_args['deprecated_args'][arg]))