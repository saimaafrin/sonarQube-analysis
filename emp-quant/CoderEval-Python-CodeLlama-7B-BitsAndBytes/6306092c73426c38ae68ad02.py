def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	deprecated_args = {}
	for arg in cli_args:
		if arg in answer_file_args:
			deprecated_args[arg] = cli_args[arg]
			print("WARNING: Argument '%s' is deprecated. Please remove it from the answer file." % arg)
		else:
			deprecated_args[arg] = cli_args[arg]
			print("WARNING: Argument '%s' is deprecated. Please remove it from the command line." % arg)
	return deprecated_args