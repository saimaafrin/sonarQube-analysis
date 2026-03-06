def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='''
		This script is used to generate a set of test cases for the given problem.
		''')
	parser.add_argument('-p', '--problem', type=str, required=True, help='The problem to generate test cases for')
	parser.add_argument('-o', '--output', type=str, required=True, help='The output file to write the test cases to')
	parser.add_argument('-n', '--num-test-cases', type=int, required=True, help='The number of test cases to generate')
	parser.add_argument('-s', '--seed', type=int, required=True, help='The seed to use for generating the test cases')
	parser.add_argument('-v', '--verbose', action='store_true', help='Print the test cases to stdout')
	return parser.parse_args(arguments)