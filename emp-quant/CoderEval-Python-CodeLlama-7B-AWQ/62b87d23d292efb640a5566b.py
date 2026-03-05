def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if not isinstance(commands, list):
		raise TypeError("commands must be a list")
	if not isinstance(args, list):
		raise TypeError("args must be a list")
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
	else:
		env = env.copy()
	env["PYTHONIOENCODING"] = "utf-8"
	env["PYTHONUNBUFFERED"] = "1"
	env["PYTHONPATH"] = os.pathsep.join(sys.path)
	env["PATH"] = os.pathsep.join(sys.path)
	env["PYTHONDONTWRITEBYTECODE"] = "1"
	env["PYTHONNOUSERSITE"] = "1"
	env["PYTHONFAULTHANDLER"] = "1"
	env["PYTHONWARNINGS"] = "ignore"
	env["PYTHONOPTIMIZE"] = "2"
	env["PYTHONMALLOC"] = "malloc"
	env["PYTHONHASHSEED"] = "0"
	env["PYTHONCASEOK"] = "1"
	env["PYTHONIOENCODING"] = "utf-8"
	env["PYTHONUTF8"] = "1"
	env["PYTHONVERBOSE"] = "1"
	env["PYTHONDEBUG"] = "1"
	env["PYTHONPROFILEIMPORTTIME"] = "1"
	env["PYTHONPROFILEIMPORTTIME"] = "1"
	env["PYTHONPROFILEIMPORTTIME"] = "1