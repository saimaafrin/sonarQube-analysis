deprecated_args = ['old_arg1', 'old_arg2']
for arg in deprecated_args:
    if arg in cli_args:
        print(f"Warning: '{arg}' is deprecated and will be removed in future versions.")
    if arg in answer_file_args:
        print(f"Warning: '{arg}' is deprecated and will be removed in future versions.")