def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='''
		This script is used to create a new user account.
		''')
	parser.add_argument('-u', '--username', help='The username of the new user', required=True)
	parser.add_argument('-p', '--password', help='The password of the new user', required=True)
	parser.add_argument('-e', '--email', help='The email of the new user', required=True)
	parser.add_argument('-n', '--name', help='The name of the new user', required=True)
	parser.add_argument('-a', '--admin', help='The new user is an admin', action='store_true')
	parser.add_argument('-d', '--debug', help='Print debug information', action='store_true')
	return parser.parse_args(arguments)