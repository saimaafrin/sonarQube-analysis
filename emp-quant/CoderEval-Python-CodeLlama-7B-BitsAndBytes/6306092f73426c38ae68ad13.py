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
# TODO: add support for ansible-playbook --list-hosts
	# TODO: add support for ansible-playbook --list-tags
	# TODO: add support for ansible-playbook --list-tasks
	# TODO: add support for ansible-playbook --syntax-check
	# TODO: add support for ansible-playbook --connection
	# TODO: add support for ansible-playbook --forks
	# TODO: add support for ansible-playbook --timeout
	# TODO: add support for ansible-playbook --private-key
	# TODO: add support for ansible-playbook --ssh-common-args
	# TODO: add support for ansible-playbook --sftp-extra-args
	# TODO: add support for ansible-playbook --scp-extra-args
	# TODO: add support for ansible-playbook --ssh-extra-args
	# TODO: add support for ansible-playbook --become
	# TODO: add support for ansible-playbook --become-user
	# TODO: add support for ansible-playbook --become-method
	# TODO: add support for ansible-playbook --ask-become-pass
	# TODO: add support for ansible-playbook --flush-cache
	# TODO: add support for ansible-playbook --vault-password-file
	# TODO: add support for ansible-playbook --vault-id
	# TODO: add support for ansible-playbook --force-color
	# TODO: add support for ansible-playbook --force-interactive
	# TODO: add support for ansible-playbook --start-at-task
	# TODO: add support for ansible-playbook --step
	# TODO: add support for ansible-playbook --check
	# TODO: add support for ansible-playbook --diff
	# TODO: add support for ansible-playbook --one-line
	# TODO: add support for ansible-playbook --tree
	# TODO: add support for ansible-playbook --version
	# TODO: add support for ansible-playbook --help
	# TODO: add support for ansible-playbook --help-