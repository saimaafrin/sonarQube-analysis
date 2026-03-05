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
	ansible_args['verbose'] = verbose
	ansible_args['extra_vars'] = extra_vars
	ansible_args['playbook_path'] = playbook_path
	ansible_args['playbook_dir'] = ir_workspace.workspace_path
	ansible_args['playbook_file'] = playbook_path
	ansible_args['playbook_name'] = playbook_path
	ansible_args['playbook_dir'] = playbook_path
	ansible_args['playbook_file'] = playbook_path
	ansible_args['playbook_name'] = playbook_path
	ansible_args['playbook_path'] = playbook_path
	ansible_args['playbook_dir'] = playbook_path
	ansible_args['playbook_file'] = playbook_path
	ansible_args['playbook_name'] = playbook_path
	ansible_args['playbook_path'] = playbook_path
	ansible_args['playbook_dir'] = playbook_path
	ansible_args['playbook_file'] = playbook_path
	ansible_args['playbook_name'] = playbook_path
	ansible_args['playbook_path'] = playbook_path
	ansible_args['playbook_dir'] = playbook_path
	ansible_args['playbook_file'] = playbook_path
	ansible_args['playbook_name'] = playbook_path
	ansible_args['playbook_path'] = playbook_path
	ansible_args['playbook_dir'] = playbook_path
	ansible_args['playbook_file'] = playbook_path
	ansible_args['playbook_name'] = playbook_path
	ansible_args['playbook_path'] = playbook_path
	ansible_args['playbook_dir'] = playbook_path
	ansible_args['playbook_file'] = playbook_path
	ansible_args['playbook_name'] = playbook_path
	ansible_args['playbook_