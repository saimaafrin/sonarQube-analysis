def subprocess_run_helper(func, *args, timeout, extra_env=None):
	"""
	Run a function in a sub-process

    Args:
            func: function, the function to be run. It must be in a module that is importable.
            *args: str. Any additional command line arguments to be passed in
                        the first argument to ``subprocess.run``.
            extra_env: dict[str, str]. Any additional environment variables to be set for the subprocess.
    Returns:
            CompletedProcess instance
	"""
	if extra_env is None:
		extra_env = {}
	env = os.environ.copy()
	env.update(extra_env)
	cmd = [sys.executable, '-m', func.__module__ + '.' + func.__name__]
	cmd.extend(args)
	return subprocess.run(cmd, env=env, timeout=timeout)