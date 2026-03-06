def get_nested_custom_and_control_args(self, args):
	"""
	Split input arguments to control nested and custom.

Controls arguments: control the IR behavior. These arguments
    will not be put into the spec yml file
Nested arguments: are used by the Ansible playbooks and will be put
    into the spec yml file.
Custom arguments: Custom ansible variables to be used instead of the
    normal nested usage.

:param args: the collected list of args.
:return: (dict, dict): flat dicts (control_args, nested_args)
	"""
	control_args = {}
	nested_args = {}
	custom_args = {}
	for arg in args:
		if arg.startswith('--'):
			if arg.startswith('--control-'):
				control_args[arg[11:]] = True
			elif arg.startswith('--nested-'):
				nested_args[arg[9:]] = True
			elif arg.startswith('--custom-'):
				custom_args[arg[9:]] = True
			else:
				raise ValueError('Unknown argument: {}'.format(arg))
		else:
			raise ValueError('Unknown argument: {}'.format(arg))
	return control_args, nested_args, custom_args