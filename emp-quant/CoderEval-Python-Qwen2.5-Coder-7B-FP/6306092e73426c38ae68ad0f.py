def get_nested_custom_and_control_args(self, args):
# Split the args into control, nested, and custom
	control_args = {}
	nested_args = {}
	custom_args = {}

	for arg in args:
		if arg.startswith('--'):
			# Control argument
			key, value = arg.split('=')
			control_args[key[2:]] = value
		elif '=' in arg:
			# Nested or custom argument
			key, value = arg.split('=')
			if key.startswith('custom_'):
				# Custom argument
				custom_args[key[7:]] = value
			else:
				# Nested argument
				nested_args[key] = value

	return control_args, nested_args, custom_args
```

This function takes a list of arguments as input and splits them into three categories: control arguments, nested arguments, and custom arguments. The control arguments are those that start with `--` and are intended to control the behavior of the IR. The nested arguments are those that do not start with `--` and are intended to be used by the Ansible playbooks. The custom arguments are those that start with `custom_` and are intended to be used instead of the normal nested usage. The function returns three dictionaries containing the split arguments.