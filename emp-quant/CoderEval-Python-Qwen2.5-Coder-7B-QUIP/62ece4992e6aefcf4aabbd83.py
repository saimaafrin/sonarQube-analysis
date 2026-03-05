import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
    """
    if isinstance(commands, list):
        commands = [commands]
    cmd = commands + args
    if verbose:
        print(f"Running command: {' '.join(cmd)}")
    if hide_stderr:
        stderr = subprocess.STDOUT
    else:
        stderr = None
    result = subprocess.run(cmd, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=stderr)
    return result.stdout, result.returncode