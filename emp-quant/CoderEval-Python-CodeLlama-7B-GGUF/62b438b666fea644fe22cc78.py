def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+',
						help='an integer for the accumulator')
	parser.add_argument('--sum', dest='accumulate', action='store_const',
						const=sum, default=max,
						help='sum the integers (default: find the max)')
	parser.add_argument('--seed', type=int, default=None,
						help='random seed')
	parser.add_argument('--verbose', '-v', action='count', default=0,
						help='increase output verbosity')
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')
	parser.add_argument('--foo', action='store_true', default=False,
						help='foo')
	parser.add_argument('--bar', action='store_true', default=False,
						help='bar')
	parser.add_argument('--baz', action='store_true', default=False,
						help='baz')
	parser.add_argument('--qux', action='store_true', default=False,
						help='qux')
	parser.add_argument('--quux', action='store_true', default=False,
						help='quux')
	parser.add_argument('--corge', action='store_true', default=False,
						help='corge')
	parser.add_argument('--grault', action='store_true', default=False,
						help='grault')
	parser.add_argument('--garply', action='store_true', default=False,
						help='garply')
	parser.add_argument('--waldo', action='store_true', default=False,
						help='waldo