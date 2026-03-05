def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="Run a command-line tool.")
	parser.add_argument("--verbose", action="store_true", help="print more information")
	subparsers = parser.add_subparsers(dest="subparser_name")
	subparsers.required = True
	subparsers.add_parser("global")
	subparsers.add_parser("test")
	subparsers.add_parser("train")
	subparsers.add_parser("predict")
	subparsers.add_parser("evaluate")
	subparsers.add_parser("visualize")
	subparsers.add_parser("compare")
	subparsers.add_parser("compare_predictions")
	subparsers.add_parser("compare_predictions_with_ground_truth")
	subparsers.add_parser("compare_predictions_with_ground_truth_and_save")
	subparsers.add_parser("compare_predictions_with_ground_truth_and_save_and_plot")
	subparsers.add_parser("compare_predictions_with_ground_truth_and_save_and_plot_and_print")
	subparsers.add_parser("compare_predictions_with_ground_truth_and_save_and_plot_and_print_and_print")
	subparsers.add_parser("compare_predictions_with_ground_truth_and_save_and_plot_and_print_and_print_and_print")
	subparsers.add_parser("compare_predictions_with_ground_truth_and_save_and_plot_and_print_and_print_and_print_and_print")
	subparsers.add_parser("compare_predictions_with_ground_truth_and_save_and_plot_and_print_and_print_and_print_and_print_and_print")
	subparsers.add_parser("compare_predictions_with_ground_truth_and_save_and_plot_and_print_and_print_and_print_and_print_and_print_and_