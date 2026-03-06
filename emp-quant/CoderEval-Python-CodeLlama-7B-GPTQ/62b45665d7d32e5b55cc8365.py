def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--input', type=str, help='Input file')
	parser.add_argument('--output', type=str, help='Output file')
	parser.add_argument('--model', type=str, help='Model file')
	parser.add_argument('--epochs', type=int, help='Number of epochs')
	parser.add_argument('--batch_size', type=int, help='Batch size')
	parser.add_argument('--learning_rate', type=float, help='Learning rate')
	parser.add_argument('--dropout', type=float, help='Dropout rate')
	parser.add_argument('--num_layers', type=int, help='Number of layers')
	parser.add_argument('--num_units', type=int, help='Number of units')
	parser.add_argument('--num_classes', type=int, help='Number of classes')
	parser.add_argument('--num_features', type=int, help='Number of features')
	parser.add_argument('--num_samples', type=int, help='Number of samples')
	parser.add_argument('--num_samples_test', type=int, help='Number of samples')
	parser.add_argument('--num_samples_val', type=int, help='Number of samples')
	parser.add_argument('--num_samples_train', type=int, help='Number of samples')
	parser.add_argument('--num_samples_test_val', type=int, help='Number of samples')
	parser.add_argument('--num_samples_train_val', type=int, help='Number of samples')
	parser.add_argument('--num_samples_test_train', type=int, help='Number of samples')
	parser.add_argument('--num_samples_val_train', type=int, help='Number of samples')
	parser.add_argument('--num_samples_test_val_train', type=int, help='Number of samples')
	parser.add_argument('--num_samples_train_val_