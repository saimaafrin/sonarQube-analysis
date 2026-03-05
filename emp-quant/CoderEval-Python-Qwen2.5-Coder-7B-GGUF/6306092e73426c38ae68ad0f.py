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
            custom_args[arg.replace('--custom-', '')] = True
        else:
            nested_args[arg] = True

    return control_args, nested_args, custom_args