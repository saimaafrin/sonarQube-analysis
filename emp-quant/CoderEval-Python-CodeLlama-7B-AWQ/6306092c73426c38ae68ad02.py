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
			print("WARNING: The argument %s is deprecated and will be removed in future versions." % arg)
			print("Please use %s instead." % self.deprecated_args[arg])
			print("")
	for arg in answer_file_args:
		if arg in self.deprecated_args:
			deprecated_args.append(arg)
			print("WARNING: The argument %s is deprecated and will be removed in future versions." % arg)
			print("Please use %s instead." % self.deprecated_args[arg])
			print("")
	if deprecated_args:
		print("")
		print("The following arguments are deprecated and will be removed in future versions:")
		for arg in deprecated_args:
			print("  %s" % arg)
		print("")