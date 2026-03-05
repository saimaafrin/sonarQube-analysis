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
	for option in options_spec:
		if option.get('required_when') and option.get('required_when')(args):
			required_args.append(option.get('name'))
	return required_args