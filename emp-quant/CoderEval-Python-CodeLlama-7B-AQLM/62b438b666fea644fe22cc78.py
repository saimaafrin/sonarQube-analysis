def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='''
		This script is used to generate a list of all the files in a directory and its subdirectories.
		''')
	parser.add_argument('-d', '--directory', help='''
		The directory to be searched.
		''', required=True)
	parser.add_argument('-o', '--output', help='''
		The output file to which the list of files will be written.
		''', required=True)
	parser.add_argument('-r', '--recursive', help='''
		If this flag is set, the script will search the directory recursively.
		''', action='store_true')
	parser.add_argument('-f', '--file', help='''
		If this flag is set, the script will search for files only.
		''', action='store_true')
	parser.add_argument('-d', '--directory', help='''
		If this flag is set, the script will search for directories only.
		''', action='store_true')
	parser.add_argument('-s', '--size', help='''
		If this flag is set, the script will search for files only.
		''', action='store_true')
	parser.add_argument('-n', '--name', help='''
		If this flag is set, the script will search for files only.
		''', action='store_true')
	parser.add_argument('-e', '--extension', help='''
		If this flag is set, the script will search for files only.
		''', action='store_true')
	parser.add_argument('-c', '--content', help='''
		If this flag is set, the script will search for files only.
		''', action='store_true')
	parser.add_argument('-v', '--verbose', help='''
		If this flag is set, the script will print the files as it finds them.
		''', action='store_true')
	parser.add_argument('-q', '--quiet', help='''