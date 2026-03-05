def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	deprecated_args = self.get_deprecated_args()
	for arg in cli_args:
		if arg in deprecated_args:
			print("WARNING: The argument '%s' is deprecated and will be removed in future versions." % arg)
			print("         Please use '%s' instead." % deprecated_args[arg])
	for arg in answer_file_args:
		if arg in deprecated_args:
			print("WARNING: The argument '%s' is deprecated and will be removed in future versions." % arg)
			print("         Please use '%s' instead." % deprecated_args[arg])