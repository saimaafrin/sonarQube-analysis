import subprocess
import os

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
    ansible_cmd = ['ansible-playbook', playbook_path]
    
    if verbose:
        ansible_cmd.append(f'-v {verbose}')
    
    if extra_vars:
        for key, value in extra_vars.items():
            ansible_cmd.append(f'-e {key}={value}')
    
    for key, value in ansible_args.items():
        ansible_cmd.append(f'-a {key}={value}')
    
    ansible_cmd.append(f'-l {ir_workspace.hosts}')
    
    result = subprocess.run(ansible_cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception(f"Ansible playbook failed: {result.stderr}")
    
    return result.stdout