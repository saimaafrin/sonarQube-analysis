import subprocess

def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Runs ansible cli with vars dict

    :param vars_dict: dict, Will be passed as Ansible extra-vars
    :param cli_args: the list of command line arguments
    :param ir_workspace: An Infrared Workspace object represents the active workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :return: ansible results
    """
    extra_vars = ['--extra-vars', ','.join([f"{key}={value}" for key, value in vars_dict.items()])]
    full_cli_args = ['ansible-playbook'] + extra_vars + cli_args
    result = subprocess.run(full_cli_args, capture_output=True, text=True)
    return result.stdout