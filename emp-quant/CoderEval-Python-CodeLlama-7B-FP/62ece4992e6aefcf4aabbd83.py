def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if verbose:
		print("Running command:", commands, args)
	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None
	if env is None:
		env = os.environ
	if isinstance(cwd, str):
		cwd = os.path.abspath(cwd)
	if isinstance(cwd, list):
		cwd = os.path.abspath(os.path.join(*cwd))
	if isinstance(cwd, tuple):
		cwd = os.path.abspath(os.path.join(*cwd))
	if isinstance(cwd, dict):
		cwd = os.path.abspath(os.path.join(*cwd.values()))
	if isinstance(cwd, Path):
		cwd = os.path.abspath(cwd)
	if isinstance(cwd, str):
		cwd = os.path.abspath(cwd)
	if isinstance(cwd, list):
		cwd = os.path.abspath(os.path.join(*cwd))
	if isinstance(cwd, tuple):
		cwd = os.path.abspath(os.path.join(*cwd))
	if isinstance(cwd, dict):
		cwd = os.path.abspath(os.path.join(*cwd.values()))
	if isinstance(cwd, Path):
		cwd = os.path.abspath(cwd)
	if isinstance(cwd, str):
		cwd = os.path.abspath(cwd)
	if isinstance(cwd, list):
		cwd = os.path.abspath(os.path.join(*cwd))
	if isinstance(cwd, tuple):
		cwd = os.path.abspath(os.path.join(*c