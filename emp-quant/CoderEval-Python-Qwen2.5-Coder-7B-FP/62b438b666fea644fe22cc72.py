def parser_flags(parser):
# Get the list of all arguments and their default values
	args = parser._actions

	# Initialize an empty string to store the argument flags
	flags = ""

	# Iterate over each argument
	for arg in args:
		# Check if the argument is optional (i.e., it has a short or long flag)
		if arg.option_strings:
			# Add the short or long flag to the string
			flags += " ".join(arg.option_strings) + " "
		else:
			# If the argument is positional, add its name to the string
			flags += arg.dest + " "

	# Return the final string of argument flags
	return flags.strip()