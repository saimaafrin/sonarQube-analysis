deprecated_args = {
    'old_arg': 'new_arg',
    'old_flag': 'new_flag',
    'old_option': 'new_option'
}

for arg, new_arg in deprecated_args.items():
    if arg in cli_args or arg in answer_file_args:
        print(f"Warning: {arg} is deprecated. Use {new_arg} instead.")