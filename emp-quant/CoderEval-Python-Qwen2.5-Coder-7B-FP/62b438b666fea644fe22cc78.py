def parse_arguments(*arguments):
# Create a new ArgumentParser object to hold the parsed arguments
	parser = argparse.ArgumentParser(description="Process some integers.")
	
	# Add each argument to the parser using add_argument method
	for arg in arguments:
		parser.add_argument(arg)
		
	# Parse the command-line arguments and store them in args variable
	args = parser.parse_args()
	
	# Return the args object containing all parsed arguments
	return args