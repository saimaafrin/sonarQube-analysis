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
	                     extra_vars=None, ansible_args=None):
ansible_args = ansible_args or {}
	ansible_args['playbook'] = playbook_path
	ansible_args['verbose'] = verbose
	ansible_args['extra_vars'] = extra_vars
	ansible_args['inventory'] = ir_workspace.get_inventory_path()
	ansible_args['connection'] = ir_workspace.get_connection_type()
	ansible_args['private_key_file'] = ir_workspace.get_private_key_path()
	ansible_args['host_key_checking'] = ir_workspace.get_host_key_checking()
	ansible_args['become'] = ir_workspace.get_become()
	ansible_args['become_user'] = ir_workspace.get_become_user()
	ansible_args['become_method'] = ir_workspace.get_become_method()
	ansible_args['become_ask_pass'] = ir_workspace.get_become_ask_pass()
	ansible_args['ask_vault_pass'] = ir_workspace.get_ask_vault_pass()
	ansible_args['vault_password_file'] = ir_workspace.get_vault_password_file()
	ansible_args['force_handlers'] = ir_workspace.get_force_handlers()
	ansible_args['flush_cache'] = ir_workspace.get_flush_cache()
	ansible_args['list_hosts'] = ir_workspace.get_list_hosts()
	ansible_args['list_tags'] = ir_workspace.get_list_tags()
	ansible_args['list_tasks'] = ir_workspace.get_list_tasks()
	ansible_args['syntax'] = ir_workspace.get_syntax()
	ansible_args['sudo'] = ir_workspace.get_sudo()
	ansible_args['sudo_user'] = ir_workspace.get_sudo_user()
	ansible_args['sudo_password'] = ir_workspace.get_sudo_password()