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
	for arg in args:
		if arg in options_spec:
			if options_spec[arg].get('required_when'):
				for condition in options_spec[arg]['required_when']:
					if condition in args:
						required_args.append(arg)
						break
	return required_args