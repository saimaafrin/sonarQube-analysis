def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	deprecated_args = []
	for arg in cli_args:
		if arg in self.deprecated_args:
			deprecated_args.append(arg)
			print("WARNING: Argument %s is deprecated and will be ignored." % arg)
	for arg in answer_file_args:
		if arg in self.deprecated_args:
			deprecated_args.append(arg)
			print("WARNING: Argument %s is deprecated and will be ignored." % arg)
	if deprecated_args:
		print("WARNING: The following arguments are deprecated and will be ignored: %s" % deprecated_args)