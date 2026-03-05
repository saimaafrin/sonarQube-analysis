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
        if arg.startswith('--control-'):
            key, value = arg.split('=', 1)
            control_args[key[len('--control-'):]] = value
        elif arg.startswith('--nested-'):
            key, value = arg.split('=', 1)
            nested_args[key[len('--nested-'):]] = value
        else:
            key, value = arg.split('=', 1)
            custom_args[key] = value

    return control_args, nested_args, custom_args