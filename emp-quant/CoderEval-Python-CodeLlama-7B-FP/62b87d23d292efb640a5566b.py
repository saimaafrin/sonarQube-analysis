def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if not isinstance(commands, list):
		raise ValueError("commands must be a list of strings")
	if not isinstance(args, list):
		raise ValueError("args must be a list of strings")
	if not commands:
		raise ValueError("commands must not be empty")
	if not args:
		raise ValueError("args must not be empty")
	if verbose:
		print("Running command:", commands, args)
	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None
	if env is None:
		env = os.environ
	try:
		subprocess.check_call(commands + args, cwd=cwd, env=env, stderr=stderr)
	except subprocess.CalledProcessError as e:
		print("Command failed:", commands, args)
		print("Exit code:", e.returncode)
		print("Output:", e.output)
		raise