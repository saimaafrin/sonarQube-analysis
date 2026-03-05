def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--input_file', type=str, help='Input file')
	parser.add_argument('--output_file', type=str, help='Output file')
	parser.add_argument('--model_file', type=str, help='Model file')
	parser.add_argument('--model_name', type=str, help='Model name')
	parser.add_argument('--model_type', type=str, help='Model type')
	parser.add_argument('--model_version', type=str, help='Model version')
	parser.add_argument('--model_description', type=str, help='Model description')
	parser.add_argument('--model_license', type=str, help='Model license')
	parser.add_argument('--model_author', type=str, help='Model author')
	parser.add_argument('--model_author_email', type=str, help='Model author email')
	parser.add_argument('--model_url', type=str, help='Model url')
	parser.add_argument('--model_keywords', type=str, help='Model keywords')
	parser.add_argument('--model_class_name', type=str, help='Model class name')
	parser.add_argument('--model_class_file', type=str, help='Model class file')
	parser.add_argument('--model_class_file_name', type=str, help='Model class file name')
	parser.add_argument('--model_class_file_url', type=str, help='Model class file url')
	parser.add_argument('--model_class_file_sha256', type=str, help='Model class file sha256')
	parser.add_argument('--model_class_file_size', type=str, help='Model class file size')
	parser.add_argument('--model_class_file_mime_type', type=str, help='Model class file mime type')
	parser.add_argument('--model_class_file_format', type=str, help='Model class file format')
	parser.add