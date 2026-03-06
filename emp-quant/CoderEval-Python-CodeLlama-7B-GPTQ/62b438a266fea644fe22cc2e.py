def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="Run a test suite.")
	subparsers = parser.add_subparsers(dest="subparser_name")
	subparsers.add_parser("global", help="Run all tests.")
	subparsers.add_parser("test", help="Run a single test.")
	subparsers.add_parser("test_suite", help="Run a test suite.")
	subparsers.add_parser("test_suite_list", help="List all test suites.")
	subparsers.add_parser("test_suite_list_tests", help="List all tests in a test suite.")
	subparsers.add_parser("test_suite_list_test_cases", help="List all test cases in a test suite.")
	subparsers.add_parser("test_suite_list_test_cases_with_test_suite", help="List all test cases in a test suite.")
	subparsers.add_parser("test_suite_list_test_cases_with_test_suite_and_test", help="List all test cases in a test suite.")
	subparsers.add_parser("test_suite_list_test_cases_with_test_suite_and_test_and_test_case", help="List all test cases in a test suite.")
	subparsers.add_parser("test_suite_list_test_cases_with_test_suite_and_test_and_test_case_and_test_case_name", help="List all test cases in a test suite.")
	subparsers.add_parser("test_suite_list_test_cases_with_test_suite_and_test_and_test_case_and_test_case_name_and_test_case_name", help="List all test cases in a test suite.")
	subparsers.add_parser("test_suite_list_test_cases_with_test_suite_and_test_and_test_case_and_test_case_name_and_test_case_name_and_test_case_name", help="List all test cases in a test suite.")
	subparsers.add_parser("test_suite_list_test_cases_with