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
	ansible_args.setdefault('inventory', ir_workspace.get_inventory_path())
	ansible_args.setdefault('connection', 'local')
	ansible_args.setdefault('module_path', ir_plugin.get_ansible_module_path())
	ansible_args.setdefault('forks', 5)
	ansible_args.setdefault('become', True)
	ansible_args.setdefault('become_method', 'sudo')
	ansible_args.setdefault('become_user', 'root')
	ansible_args.setdefault('ask_sudo_pass', False)
	ansible_args.setdefault('ask_pass', False)
	ansible_args.setdefault('vault_password_file', ir_workspace.get_vault_password_path())
	ansible_args.setdefault('verbosity', verbose)
	ansible_args.setdefault('extra_vars', extra_vars)
	ansible_args.setdefault('playbook', playbook_path)
	ansible_args.setdefault('syntax', True)
	ansible_args.setdefault('list_hosts', False)
	ansible_args.setdefault('list_tags', False)
	ansible_args.setdefault('list_tasks', False)
	ansible_args.setdefault('skip_tags', None)
	ansible_args.setdefault('start_at_task', None)
	ansible_args.setdefault('step', False)
	ansible_args.setdefault('tree', False)
	ansible_args.setdefault('force_handlers', False)
	ansible_args.setdefault('flush_cache', False)
	ansible_args.setdefault('version', False)
	ansible_args.setdefault('help', False)
	ansible_args.setdefault('check', False)
	ansible_args.setdefault('syntax_check', False)
	ansible_args.setdefault('one_line', False)
	ansible_args.setdefault('sudo_user', None)