import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    if hide_stderr:
        stderr = subprocess.DEVNULL
    else:
        stderr = subprocess.STDOUT
    
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)}")
        result = subprocess.run(full_command, cwd=cwd, stderr=stderr, env=env, text=True)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, full_command, output=result.stdout)
        if verbose:
            print(f"Command output: {result.stdout}")