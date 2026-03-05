def validate_arg_deprecation(self, cli_args, answer_file_args):
    deprecated_args = ['old_arg1', 'old_arg2']
    for arg in deprecated_args:
        if arg in cli_args:
            print(f"Warning: '{arg}' is deprecated. Please use the new argument instead.")
        if arg in answer_file_args:
            print(f"Warning: '{arg}' is deprecated. Please use the new argument instead.")