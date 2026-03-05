def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
This function takes in several parameters including `cli_args`, `vars_dict`, `ir_workspace`, and `ir_plugin`. It creates a temporary file to store the `vars_dict` as JSON. Then it appends the `--extra-vars` option to the `cli_args` list pointing to the temporary file. After that, it runs the playbook using the `ansible-playbook` command and captures the output. Finally, it removes the temporary file and returns the captured output.

You can use this function by passing in the appropriate arguments. For example: