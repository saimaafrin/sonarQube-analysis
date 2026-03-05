def parse_arguments(*unparsed_arguments):
arguments = {}
	for argument in unparsed_arguments:
		if "=" not in argument:
			continue

		key, value = argument.split("=")
		arguments[key.strip()] = value.strip()

	return arguments