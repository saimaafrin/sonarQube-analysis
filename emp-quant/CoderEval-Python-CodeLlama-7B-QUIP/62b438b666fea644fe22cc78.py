def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description="This script is used to parse the arguments for the script")
	parser.add_argument("--input", "-i", help="The input file to be parsed")
	parser.add_argument("--output", "-o", help="The output file to be parsed")
	parser.add_argument("--verbose", "-v", help="The verbose option")
	parser.add_argument("--debug", "-d", help="The debug option")
	parser.add_argument("--help", "-h", help="The help option")
	parser.add_argument("--version", "-V", help="The version option")
	parser.add_argument("--log", "-l", help="The log option")
	parser.add_argument("--log-file", "-L", help="The log file option")
	parser.add_argument("--log-dir", "-D", help="The log directory option")
	parser.add_argument("--log-level", "-L", help="The log level option")
	parser.add_argument("--log-format", "-F", help="The log format option")
	parser.add_argument("--log-type", "-T", help="The log type option")
	parser.add_argument("--log-path", "-P", help="The log path option")
	parser.add_argument("--log-service", "-S", help="The log service option")
	parser.add_argument("--log-server", "-S", help="The log server option")
	parser.add_argument("--log-port", "-P", help="The log port option")
	parser.add_argument("--log-protocol", "-P", help="The log protocol option")
	parser.add_argument("--log-level", "-L", help="The log level option")
	parser.add_argument("--log-format", "-F", help="The log format option")
	parser.add_argument("--log-type", "-T", help="The log type option")
	parser.add_argument("--log-path", "-P", help="The log path option")
	parser.add_argument("--log-service", "-S", help="The log service