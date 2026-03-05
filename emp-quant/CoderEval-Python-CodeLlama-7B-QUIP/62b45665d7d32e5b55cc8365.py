def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_file", help="Input file", default=None)
	parser.add_argument("--output_file", help="Output file", default=None)
	parser.add_argument("--input_format", help="Input format", default=None)
	parser.add_argument("--output_format", help="Output format", default=None)
	parser.add_argument("--input_format_options", help="Input format options", default=None)
	parser.add_argument("--output_format_options", help="Output format options", default=None)
	parser.add_argument("--input_format_options_file", help="Input format options file", default=None)
	parser.add_argument("--output_format_options_file", help="Output format options file", default=None)
	parser.add_argument("--input_format_options_file_type", help="Input format options file type", default=None)
	parser.add_argument("--output_format_options_file_type", help="Output format options file type", default=None)
	parser.add_argument("--input_format_options_file_type_options", help="Input format options file type options", default=None)
	parser.add_argument("--output_format_options_file_type_options", help="Output format options file type options", default=None)
	parser.add_argument("--input_format_options_file_type_options_file", help="Input format options file type options file", default=None)
	parser.add_argument("--output_format_options_file_type_options_file", help="Output format options file type options file", default=None)
	parser.add_argument("--input_format_options_file_type_options_file_type", help="Input format options file type options file type", default=None)
	parser.add_argument("--output_format_options_file_type_options_file_type", help="Output format options file type options file type", default=None)
	parser.add_argument("--input_format_options_file_type_options_