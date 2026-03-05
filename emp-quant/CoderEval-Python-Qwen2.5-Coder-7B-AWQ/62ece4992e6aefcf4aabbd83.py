import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
    """
    if isinstance(commands, str):
        commands = [commands]
    
    if isinstance(args, str):
        args = [args]
    
    if hide_stderr:
        stderr = subprocess.DEVNULL
    else:
        stderr = subprocess.STDOUT
    
    process = subprocess.Popen([*commands, *args], cwd=cwd, stdout=subprocess.PIPE, stderr=stderr, env=env)
    stdout, _ = process.communicate()
    
    if verbose:
        print(f"Command: {' '.join([*commands, *args])}")
        print(f"CWD: {cwd}")
        print(f"Environment: {env}")
        print(f"Output: {stdout.decode('utf-8')}")
    
    return stdout, process.returncode