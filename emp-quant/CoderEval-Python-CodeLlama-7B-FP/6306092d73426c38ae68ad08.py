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
	for arg in options_spec:
		if arg.get('required_when'):
			if arg['required_when'] in args:
				required_args.append(arg['name'])
	return required_args