def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--input_file', type=str, help='Input file')
	parser.add_argument('--output_file', type=str, help='Output file')
	parser.add_argument('--input_format', type=str, help='Input format')
	parser.add_argument('--output_format', type=str, help='Output format')
	parser.add_argument('--input_delimiter', type=str, help='Input delimiter')
	parser.add_argument('--output_delimiter', type=str, help='Output delimiter')
	parser.add_argument('--input_quotechar', type=str, help='Input quotechar')
	parser.add_argument('--output_quotechar', type=str, help='Output quotechar')
	parser.add_argument('--input_escapechar', type=str, help='Input escapechar')
	parser.add_argument('--output_escapechar', type=str, help='Output escapechar')
	parser.add_argument('--input_header', type=str, help='Input header')
	parser.add_argument('--output_header', type=str, help='Output header')
	parser.add_argument('--input_null_value', type=str, help='Input null value')
	parser.add_argument('--output_null_value', type=str, help='Output null value')
	parser.add_argument('--input_nan_value', type=str, help='Input nan value')
	parser.add_argument('--output_nan_value', type=str, help='Output nan value')
	parser.add_argument('--input_pos_inf_value', type=str, help='Input pos inf value')
	parser.add_argument('--output_pos_inf_value', type=str, help='Output pos inf value')
	parser.add_argument('--input_neg_inf_value', type=str, help='Input neg inf value')
	parser.add_argument('--output_neg_inf_value', type=str, help='Output neg inf value')
	parser.add_argument('--input_