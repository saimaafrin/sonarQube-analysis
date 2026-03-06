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
	# TODO: add support for playbook file
	# TODO: add support for playbook dir
	# TODO: add support for playbook dir and playbook file
	# TODO: add support for playbook dir and playbook file and playbook name
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars and tags
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars and tags and skip-tags
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars and tags and skip-tags and start-at-task
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars and tags and skip-tags and start-at-task and
	# become
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars and tags and skip-tags and start-at-task and
	# become and become-method
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars and tags and skip-tags and start-at-task and
	# become and become-method and verbosity
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars and tags and skip-tags and start-at-task and
	# become and become-method and verbosity and remote-user
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory and extra-vars and tags and skip-tags and start-at-task and
	# become and become-method and verbosity and remote-user and ssh-common-args
	# TODO: add support for playbook dir and playbook file and playbook name and
	# inventory