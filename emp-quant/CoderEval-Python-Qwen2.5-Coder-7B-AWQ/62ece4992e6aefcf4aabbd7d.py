import subprocess
from typing import Callable, Dict, Tuple

def subprocess_run_helper(func: Callable, *args: str, timeout: int, extra_env: Dict[str, str] = None) -> subprocess.CompletedProcess:
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
    # Construct the command to run the function
    command = [func.__module__ + '.' + func.__name__]
    command.extend(args)

    # Set up the environment variables
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Run the subprocess
    result = subprocess.run(command, timeout=timeout, check=True, env=env, capture_output=True, text=True)
    return result