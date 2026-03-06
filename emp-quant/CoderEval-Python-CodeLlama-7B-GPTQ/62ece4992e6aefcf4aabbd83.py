def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if not isinstance(commands, list):
		raise ValueError("commands must be a list")
	if not isinstance(args, list):
		raise ValueError("args must be a list")
	if len(commands) != len(args):
		raise ValueError("commands and args must have the same length")
	if verbose:
		print("Running command:", commands, args)
	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None
	if env is None:
		env = os.environ
	result = []
	for command, arg in zip(commands, args):
		result.append(subprocess.run([command] + arg.split(), cwd=cwd, env=env, stderr=stderr))
	return result