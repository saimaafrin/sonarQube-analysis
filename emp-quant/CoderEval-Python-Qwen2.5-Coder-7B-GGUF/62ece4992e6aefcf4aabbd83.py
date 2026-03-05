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
    
    process = subprocess.Popen([commands[0]] + args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=stderr)
    stdout, stderr = process.communicate()
    
    if verbose:
        print(f"Command: {' '.join([commands[0]] + args)}")
        print(f"Stdout: {stdout.decode()}")
        if not hide_stderr:
            print(f"Stderr: {stderr.decode()}")
    
    return stdout, process.returncode