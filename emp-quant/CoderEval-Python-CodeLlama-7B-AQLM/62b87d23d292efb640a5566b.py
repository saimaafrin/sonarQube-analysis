def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, str):
		commands = [commands]

	if verbose:
		print("Running command:", commands)

	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None

	if env is None:
		env = os.environ

	try:
		proc = subprocess.Popen(commands, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=stderr)
	except OSError as e:
		print("Error running command:", commands)
		print(e)
		return False

	if args is None:
		args = []

	if isinstance(args, str):
		args = [args]

	if verbose:
		print("Running command with args:", args)

	try:
		proc.communicate(args)
	except OSError as e:
		print("Error running command:", commands)
		print(e)
		return False

	if proc.returncode != 0:
		print("Error running command:", commands)
		print("Return code:", proc.returncode)
		return False

	return True