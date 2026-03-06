def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if not isinstance(commands, list):
		raise ValueError("commands must be a list")
	if not isinstance(args, list):
		raise ValueError("args must be a list")
	if not commands:
		raise ValueError("commands must not be empty")
	if not args:
		raise ValueError("args must not be empty")
	if cwd is not None and not isinstance(cwd, str):
		raise ValueError("cwd must be a string or None")
	if not isinstance(verbose, bool):
		raise ValueError("verbose must be a boolean")
	if not isinstance(hide_stderr, bool):
		raise ValueError("hide_stderr must be a boolean")
	if env is not None and not isinstance(env, dict):
		raise ValueError("env must be a dict or None")
	if verbose:
		print("Running command:", commands, args)
	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None
	if env is None:
		env = os.environ
	else:
		env = env.copy()
	env.update(os.environ)
	try:
		subprocess.check_call(commands + args, cwd=cwd, env=env, stderr=stderr)
	except subprocess.CalledProcessError as e:
		print("Command failed:", commands, args)
		print("Exit code:", e.returncode)
		print("Output:", e.output)
		raise