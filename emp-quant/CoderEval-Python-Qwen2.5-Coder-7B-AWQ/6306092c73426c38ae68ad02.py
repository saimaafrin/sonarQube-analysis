import logging

class DeprecatedArgumentValidator:
    def __init__(self):
        self.deprecated_args = {
            'old_arg': 'new_arg',
            # Add more deprecated arguments here
        }

    def validate_arg_deprecation(self, cli_args, answer_file_args):
        """
        Validates and prints the deprecated arguments.

        :param cli_args: the dict of arguments from cli
        :param answer_file_args:  the dict of arguments from files
        """
        for arg, value in {**cli_args, **answer_file_args}.items():
            if arg in self.deprecated_args:
                new_arg = self.deprecated_args[arg]
                logging.warning(f"Deprecated argument '{arg}' used. Please use '{new_arg}' instead.")