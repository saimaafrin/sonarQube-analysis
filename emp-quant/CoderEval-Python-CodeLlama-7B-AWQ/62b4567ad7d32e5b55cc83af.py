def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='''
		This script is used to create a new user in the database.
		''')
	parser.add_argument('-u', '--username', help='The username of the new user', required=True)
	parser.add_argument('-p', '--password', help='The password of the new user', required=True)
	parser.add_argument('-e', '--email', help='The email of the new user', required=True)
	parser.add_argument('-n', '--name', help='The name of the new user', required=True)
	parser.add_argument('-a', '--admin', help='Whether the new user is an admin or not', required=True)
	return parser.parse_args(arguments)