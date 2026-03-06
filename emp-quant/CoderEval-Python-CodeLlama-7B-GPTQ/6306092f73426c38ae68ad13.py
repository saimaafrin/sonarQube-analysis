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
	ansible_args = ansible_args or {}
	ansible_args.setdefault('inventory', ir_workspace.inventory_path)
	ansible_args.setdefault('connection', 'local')
	ansible_args.setdefault('vault_password_file', ir_workspace.vault_path)
	ansible_args.setdefault('extra_vars', extra_vars)
	ansible_args.setdefault('verbose', verbose)
	ansible_args.setdefault('playbook', playbook_path)
	ansible_args.setdefault('become', True)
	ansible_args.setdefault('become_user', 'root')
	ansible_args.setdefault('become_method', 'sudo')
	ansible_args.setdefault('become_exe', '/bin/sh')
	ansible_args.setdefault('become_prompt', '[sudo via ansible, key=%s] password: ' % ir_plugin.name)
	ansible_args.setdefault('ask_become_pass', True)
	ansible_args.setdefault('ask_pass', True)
	ansible_args.setdefault('ask_sudo', True)
	ansible_args.setdefault('sudo_user', 'root')
	ansible_args.setdefault('sudo_exe', '/bin/sh')
	ansible_args.setdefault('sudo_prompt', '[sudo via ansible, key=%s] password: ' % ir_plugin.name)
	ansible_args.setdefault('sudo_pass', True)
	ansible_args.setdefault('sudo_prompt_pass', True)
	ansible_args.setdefault('sudo_user', 'root')
	ansible_args.setdefault('sudo_exe', '/bin/sh')
	ansible_args.setdefault('sudo_prompt', '[sudo via ansible, key=%s] password: ' % ir_plugin.name)
	ansible_args.setdefault('sudo_pass', True)
	ansible_args.setdefault('sudo_prompt_pass', True)
	ansible_args.setdefault('sudo_