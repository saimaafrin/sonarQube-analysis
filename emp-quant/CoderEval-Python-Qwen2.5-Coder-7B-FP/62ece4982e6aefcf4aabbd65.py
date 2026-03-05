def parser_flags(parser):
# Get the list of all arguments and their default values
	args = parser._actions[1:]
	flags = []
	for arg in args:
		if arg.nargs == 0:
			flag = f"--{arg.dest}"
			default_value = arg.default
			if default_value is not None:
				flag += f"={default_value}"
			flags.append(flag)
	return " ".join(flags)