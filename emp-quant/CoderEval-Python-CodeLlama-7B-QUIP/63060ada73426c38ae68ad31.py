def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	# Get the parser
	parser = self.get_parser(parser_name)
	# Get the arguments
	args = parser.get_arguments()
	# Loop through the arguments
	for arg in args:
		# Get the value
		value = values_dict[arg.name]
		# Check if the value is a list
		if arg.type == list:
			# Loop through the list
			for i in range(len(value)):
				# Check if the value is a list
				if arg.type == list:
					# Loop through the list
					for j in range(len(value[i])):
						# Check if the value is a list
						if arg.type == list:
							# Loop through the list
							for k in range(len(value[i][j])):
								# Check if the value is a list
								if arg.type == list:
									# Loop through the list
									for l in range(len(value[i][j][k])):
										# Check if the value is a list
										if arg.type == list:
											# Loop through the list
											for m in range(len(value[i][j][k][l])):
												# Check if the value is a list
												if arg.type == list:
													# Loop through the list
													for n in range(len(value[i][j][k][l][m])):
														# Check if the value is a list