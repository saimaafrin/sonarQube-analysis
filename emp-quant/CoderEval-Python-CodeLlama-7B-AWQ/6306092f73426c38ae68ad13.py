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
	ansible_args['inventory'] = ir_workspace.inventory_path
	ansible_args['playbook'] = playbook_path
	ansible_args['verbose'] = verbose
	ansible_args['extra_vars'] = extra_vars
	ansible_args['connection'] = 'local'
	ansible_args['module_path'] = ir_plugin.module_path
	ansible_args['forks'] = 1
	ansible_args['become'] = True
	ansible_args['become_user'] = 'root'
	ansible_args['become_method'] = 'sudo'
	ansible_args['become_flags'] = '-H -S -k'
	ansible_args['ask_sudo_pass'] = True
	ansible_args['ask_pass'] = True
	ansible_args['sudo_user'] = 'root'
	ansible_args['sudo_flags'] = '-H -S -k'
	ansible_args['sudo_exe'] = '/usr/bin/sudo'
	ansible_args['sudo_path'] = '/usr/bin:/usr/sbin:/sbin:/bin'
	ansible_args['sudo_pty'] = True
	ansible_args['sudo_args'] = '-H -S -k'
	ansible_args['sudo_pass'] = None
	ansible_args['sftp_batch_mode'] = True
	ansible_args['sftp_batch_size'] = 10000
	ansible_args['ssh_args'] = '-o ControlMaster=auto -o ControlPersist=60s'
	ansible_args['scp_args'] = '-o ControlMaster=auto -o ControlPersist=60s'
	ansible_args['ssh_executable'] = '/usr/bin/ssh'
	ansible_args['ssh_keysize'] = 16384
	ansible_args['ssh_type'] = 'paramiko'
	ansible_args['ssh_pipelining'] = True
	ansible_args['ssh_args'] =