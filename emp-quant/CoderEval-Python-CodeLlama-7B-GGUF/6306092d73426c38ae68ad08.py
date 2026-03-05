def _get_conditionally_required_args(self, command_name, options_spec,
                                         args):
	"""
	List arguments with ``required_when`` condition matched.

:param command_name: the command name.
:param options_spec:  the list of command spec options.
:param args: the received input arguments
:return: list, list of argument names with matched ``required_when``
    condition
	"""
	required_args = []
	for arg_name, arg_spec in options_spec.items():
		if arg_name in args:
			continue
		if arg_spec.get('required_when', None) is None:
			continue
		if not isinstance(arg_spec['required_when'], list):
			raise ValueError(
				'required_when must be a list of tuples')
		for condition in arg_spec['required_when']:
			if condition[0] == command_name:
				if condition[1] in args:
					required_args.append(arg_name)
					break
	return required_args