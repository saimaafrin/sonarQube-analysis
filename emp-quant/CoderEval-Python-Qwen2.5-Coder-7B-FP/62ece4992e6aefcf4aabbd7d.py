def subprocess_run_helper(func, *args, timeout, extra_env=None):
# Importing here to avoid circular imports
	import subprocess

	cmd = [func.__module__ + '.' + func.__name__] + list(args)
	if extra_env:
		result = subprocess.run(cmd, env={**os.environ, **extra_env}, timeout=timeout)
	else:
		result = subprocess.run(cmd, timeout=timeout)

	return result