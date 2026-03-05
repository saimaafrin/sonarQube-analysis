def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='''
		This script is used to generate a list of all the files in a directory and its subdirectories.
		''')
	parser.add_argument('-d', '--directory', type=str, help='''
		The directory to start the search from.
		''')
	parser.add_argument('-r', '--recursive', action='store_true', help='''
		If set, the search will be recursive.
		''')
	parser.add_argument('-e', '--extension', type=str, help='''
		The extension of the files to search for.
		''')
	parser.add_argument('-o', '--output', type=str, help='''
		The output file to write the list of files to.
		''')
	parser.add_argument('-v', '--verbose', action='store_true', help='''
		If set, the script will print out the files it finds.
		''')
	return parser.parse_args(arguments)