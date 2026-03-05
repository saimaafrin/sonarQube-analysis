def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--input_file', type=str, help='Input file')
	parser.add_argument('--output_file', type=str, help='Output file')
	parser.add_argument('--output_file_format', type=str, help='Output file format')
	parser.add_argument('--output_file_compression', type=str, help='Output file compression')
	parser.add_argument('--output_file_compression_level', type=int, help='Output file compression level')
	parser.add_argument('--output_file_compression_type', type=str, help='Output file compression type')
	parser.add_argument('--output_file_compression_block_size', type=int, help='Output file compression block size')
	parser.add_argument('--output_file_compression_block_size_type', type=str, help='Output file compression block size type')
	parser.add_argument('--output_file_compression_block_size_unit', type=str, help='Output file compression block size unit')
	parser.add_argument('--output_file_compression_block_size_unit_type', type=str, help='Output file compression block size unit type')
	parser.add_argument('--output_file_compression_block_size_unit_value', type=int, help='Output file compression block size unit value')
	parser.add_argument('--output_file_compression_block_size_unit_value_type', type=str, help='Output file compression block size unit value type')
	parser.add_argument('--output_file_compression_block_size_unit_value_unit', type=str, help='Output file compression block size unit value unit')
	parser.add_argument('--output_file_compression_block_size_unit_value_unit_type', type=str, help='Output file compression block size unit value unit type')
	parser.add_argument('--output_file_compression_block_size_unit_value_unit_value', type=int, help='Output file compression block size unit value unit value')
	parser