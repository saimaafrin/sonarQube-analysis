def get_silent_args(self, args):
	"""
	list of silenced argument

:param args: The received arguments.
:return: list, slienced argument names
	"""
	silent_args = []
	for arg in args:
		if arg.startswith('--silent'):
			silent_args.append(arg.split('=')[1])
	return silent_args