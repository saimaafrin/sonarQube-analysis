def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list):
		commands = [commands]
	if not isinstance(args, list):
		args = [args]
	if not isinstance(cwd, str):
		cwd = None
	if not isinstance(verbose, bool):
		verbose = False
	if not isinstance(hide_stderr, bool):
		hide_stderr = False
	if not isinstance(env, dict):
		env = None

	if verbose:
		print("Running command:")
		print(" ".join(commands))
		print(" ".join(args))
		print("Working directory:", cwd)
		print("Environment:", env)

	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None

	if env is None:
		env = os.environ

	process = subprocess.Popen(commands + args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=stderr)
	stdout, stderr = process.communicate()
	stdout = stdout.decode("utf-8")
	returncode = process.returncode

	if verbose:
		print("Return code:", returncode)
		print("Stdout:")
		print(stdout)
		print("Stderr:")
		print(stderr)

	return returncode, stdout