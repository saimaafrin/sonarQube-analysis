def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if env is None:
		env = os.environ
	if cwd is None:
		cwd = os.getcwd()
	if verbose:
		print("Running command: %s" % " ".join(commands))
		print("With arguments: %s" % " ".join(args))
		print("In directory: %s" % cwd)
		print("Environment: %s" % env)
	if hide_stderr:
		with open(os.devnull, 'w') as devnull:
			return subprocess.check_call(commands, cwd=cwd, stderr=devnull, stdout=subprocess.PIPE, stdin=subprocess.PIPE, env=env)
	else:
		return subprocess.check_call(commands, cwd=cwd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, env=env)