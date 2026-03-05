def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if env is None:
		env = {}
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if cwd is None:
		cwd = os.getcwd()
	if not isinstance(commands, list):
		commands = [commands]
	if not isinstance(args, list):
		args = [args]
	if not isinstance(env, dict):
		env = {}
	if not isinstance(cwd, str):
		cwd = os.getcwd()
	if not isinstance(verbose, bool):
		verbose = False
	if not isinstance(hide_stderr, bool):
		hide_stderr = False
	if not isinstance(env, dict):
		env = {}
	if not isinstance(cwd, str):
		cwd = os.getcwd()
	if not isinstance(verbose, bool):
		verbose = False
	if not isinstance(hide_stderr, bool):
		hide_stderr = False
	if not isinstance(env, dict):
		env = {}
	if not isinstance(cwd, str):
		cwd = os.getcwd()
	if not isinstance(verbose, bool):
		verbose = False
	if not isinstance(hide_stderr, bool):
		hide_stderr = False
	if not isinstance(env, dict):
		env = {}
	if not isinstance(cwd, str):
		cwd = os.getcwd()
	if not isinstance(verbose, bool):
		verbose = False
	if not isinstance(hide_stderr, bool):
		hide_stderr = False
	if not isinstance(env, dict):
		env = {}
	if not isinstance(cwd, str):
		cwd = os.getcwd()
	if not isinstance(verbose, bool):
		verbose = False
	if not isinstance(hide_stderr, bool):