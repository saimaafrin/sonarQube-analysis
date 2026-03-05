def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if isinstance(cwd, str):
		cwd = os.path.abspath(cwd)
	if env is None:
		env = os.environ
	if verbose:
		print("Running command:", commands, args, cwd, env)
	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None
	p = subprocess.Popen(commands + args, cwd=cwd, env=env, stderr=stderr, stdout=subprocess.PIPE)
	stdout, stderr = p.communicate()
	returncode = p.returncode
	if verbose:
		print("Return code:", returncode)
		print("Stdout:", stdout.decode())
		print("Stderr:", stderr.decode())
	return stdout.decode(), returncode