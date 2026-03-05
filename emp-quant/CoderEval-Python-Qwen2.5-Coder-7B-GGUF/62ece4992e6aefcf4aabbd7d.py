import subprocess
import importlib

def subprocess_run_helper(func, *args, timeout, extra_env=None):
    module_name, func_name = func.__module__, func.__name__
    module = importlib.import_module(module_name)
    func_to_run = getattr(module, func_name)
    cmd = [func_to_run.__name__] + list(args)
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    return subprocess.run(cmd, timeout=timeout, env=env)