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
	parser.add_argument('--hidden_size', type=int, help='Hidden size')
	parser.add_argument('--hidden_layers', type=int, help='Number of hidden layers')
	parser.add_argument('--activation', type=str, help='Activation function')
	parser.add_argument('--optimizer', type=str, help='Optimizer')
	parser.add_argument('--loss', type=str, help='Loss function')
	parser.add_argument('--metrics', type=str, help='Metrics')
	parser.add_argument('--verbose', type=int, help='Verbose')
	parser.add_argument('--callbacks', type=str, help='Callbacks')
	parser.add_argument('--callbacks_args', type=str, help='Callbacks args')
	parser.add_argument('--callbacks_kwargs', type=str, help='Callbacks kwargs')
	parser.add_argument('--callbacks_order', type=str, help='Callbacks order')
	parser.add_argument('--callbacks_trigger', type=str, help='Callbacks trigger')
	parser.add_argument('--callbacks_trigger_args', type=str, help='Callbacks trigger args')
	parser.add_argument('--callbacks_trigger_kwargs', type=str, help='Callbacks trigger kwargs')
	parser.add_argument('--callbacks_trigger_order', type=str