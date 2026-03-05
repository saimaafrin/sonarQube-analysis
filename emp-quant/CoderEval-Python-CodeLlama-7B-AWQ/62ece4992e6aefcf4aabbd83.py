def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if not isinstance(commands, list):
		raise TypeError("commands must be a list of strings")
	if not isinstance(args, list):
		raise TypeError("args must be a list of strings")
	if not isinstance(cwd, str) and cwd is not None:
		raise TypeError("cwd must be a string or None")
	if not isinstance(verbose, bool):
		raise TypeError("verbose must be a boolean")
	if not isinstance(hide_stderr, bool):
		raise TypeError("hide_stderr must be a boolean")
	if not isinstance(env, dict) and env is not None:
		raise TypeError("env must be a dictionary or None")

	if verbose:
		print("Running command:", commands, args)
		if cwd is not None:
			print("Working directory:", cwd)
		if env is not None:
			print("Environment:", env)

	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None

	if env is None:
		env = os.environ

	p = subprocess.Popen(commands + args, cwd=cwd, env=env, stderr=stderr)
	stdout, stderr = p.communicate()
	returncode = p.returncode

	if verbose:
		print("Return code:", returncode)
		print("Stdout:", stdout)
		print("Stderr:", stderr)

	return stdout, returncode