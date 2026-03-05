def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
	"""
	Runs ansible cli with vars dict

:param vars_dict: dict, Will be passed as Ansible extra-vars
:param cli_args: the list  of command line arguments
:param ir_workspace: An Infrared Workspace object represents the active
 workspace
:param ir_plugin: An InfraredPlugin object of the current plugin
:return: ansible results
	"""
	# Get the ansible cli
	ansible_cli = ir_workspace.get_ansible_cli()
	# Get the ansible playbook
	ansible_playbook = ir_workspace.get_ansible_playbook()
	# Get the ansible playbook
	ansible_inventory = ir_workspace.get_ansible_inventory()
	# Get the ansible playbook
	ansible_config = ir_workspace.get_ansible_config()
	# Get the ansible playbook
	ansible_vault = ir_workspace.get_ansible_vault()
	# Get the ansible playbook
	ansible_key = ir_workspace.get_ansible_key()
	# Get the ansible playbook
	ansible_host = ir_workspace.get_ansible_host()
	# Get the ansible playbook
	ansible_user = ir_workspace.get_ansible_user()
	# Get the ansible playbook
	ansible_password = ir_workspace.get_ansible_password()
	# Get the ansible playbook
	ansible_become = ir_workspace.get_ansible_become()
	# Get the ansible playbook
	ansible_become_pass = ir_workspace.get_ansible_become_pass()
	# Get the ansible playbook
	ansible_become_method = ir_workspace.get_ansible_become_method()
	# Get the ansible playbook
	ansible_become_user = ir_workspace.get_ansible_become_user()
	# Get the ansible playbook
	ansible_become_password = ir_workspace.get_ansible_become_password()
	# Get the ansible playbook
	ansible_become_vault = ir_workspace.get_ansible_become_vault()
	# Get the ansible playbook
	ansible_become_key = ir_workspace.get_ansible_become_key()
	# Get the ansible playbook
	ansible_become_host = ir_