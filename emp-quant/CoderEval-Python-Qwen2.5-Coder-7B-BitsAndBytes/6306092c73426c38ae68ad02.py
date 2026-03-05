import warnings

class DeprecatedArgumentWarning(Warning):
    pass

def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Validates and prints the deprecated arguments.

    :param cli_args: the dict of arguments from cli
    :param answer_file_args:  the dict of arguments from files
    """
    deprecated_args = {
        'old_arg1': 'new_arg1',
        'old_arg2': 'new_arg2'
    }

    for arg, value in {**cli_args, **answer_file_args}.items():
        if arg in deprecated_args:
            new_arg = deprecated_args[arg]
            warnings.warn(f"The argument '{arg}' is deprecated. Use '{new_arg}' instead.", DeprecatedArgumentWarning)