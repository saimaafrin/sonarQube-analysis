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
	                                         args):
required_args = []
	for arg_name, arg_spec in options_spec.items():
		if arg_name in args:
			continue
		if 'required_when' in arg_spec:
			for condition_arg_name, condition_value in arg_spec['required_when'].items():
				if condition_arg_name in args and args[condition_arg_name] == condition_value:
					required_args.append(arg_name)
					break
	return required_args