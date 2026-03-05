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
    # Construct the ansible command with extra-vars from vars_dict
    ansible_cmd = ['ansible-playbook'] + cli_args + ['-e', ','.join([f'{key}={value}' for key, value in vars_dict.items()])]
    
    # Execute the ansible command using subprocess
    result = subprocess.run(ansible_cmd, capture_output=True, text=True)
    
    return result.stdout