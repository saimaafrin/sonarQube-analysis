def parse_subparser_arguments(unparsed_arguments, subparsers):
# Initialize an empty dictionary to store parsed namespaces for each subparser
	parsed_namespaces = {subparser_name: None for subparser_name in subparsers}
	
	# Iterate over each unparsed argument
	for arg in unparsed_arguments:
		# Check if the current argument is a subcommand
		if arg in subparsers:
			# Get the corresponding subparser
			subparser = subparsers[arg]
			
			# Attempt to parse the remaining arguments using the subparser
			namespace, remaining_args = subparser.parse_known_args(unparsed_arguments[unparsed_arguments.index(arg):])
			
			# Store the parsed namespace in the dictionary
			parsed_namespaces[subparser.name] = namespace
			
			# Update the unparsed arguments with the remaining ones
			unparsed_arguments = remaining_args
	
	return parsed_namespaces, unparsed_arguments