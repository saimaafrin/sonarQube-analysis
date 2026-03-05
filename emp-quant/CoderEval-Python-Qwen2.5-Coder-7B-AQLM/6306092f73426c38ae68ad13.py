import subprocess

def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                     extra_vars=None, ansible_args=None):
    """
    Wraps the 'ansible-playbook' CLI.

    :param ir_workspace: An Infrared Workspace object represents the active
    workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :param playbook_path: the playbook to invoke
    :param verbose: Ansible verbosity level
    :param extra_vars: dict. Passed to Ansible as extra-vars
    :param ansible_args: dict of ansible-playbook arguments to plumb down
        directly to Ansible.
    """
    command = ['ansible-playbook', playbook_path]
    
    if verbose:
        command.extend(['-v'] * verbose)
    
    if extra_vars:
        for key, value in extra_vars.items():
            command.extend(['-e', f'{key}={value}'])
    
    if ansible_args:
        command.extend(list(ansible_args.items()))
    
    subprocess.run(command, check=True)