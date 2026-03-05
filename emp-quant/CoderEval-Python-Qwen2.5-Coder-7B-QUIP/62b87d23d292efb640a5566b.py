import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    if verbose:
        print(f"Running command: {' '.join(commands + args)}")
    
    env_vars = os.environ.copy()
    if env:
        env_vars.update(env)
    
    result = subprocess.run(
        commands + args,
        cwd=cwd,
        env=env_vars,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT if not hide_stderr else subprocess.DEVNULL,
        text=True
    )
    
    if result.returncode != 0 and not hide_stderr:
        print(result.stdout)
    
    return result.returncode, result.stdout