def get_nested_custom_and_control_args(self, args):
    control_args = {}
    nested_args = {}
    custom_args = {}

    for arg in args:
        if arg.startswith('--control-'):
            control_args[arg.replace('--control-', '')] = True
        elif arg.startswith('--nested-'):
            nested_args[arg.replace('--nested-', '')] = True
        elif arg.startswith('--custom-'):
            key, value = arg.replace('--custom-', '').split('=')
            custom_args[key] = value

    return control_args, nested_args, custom_args