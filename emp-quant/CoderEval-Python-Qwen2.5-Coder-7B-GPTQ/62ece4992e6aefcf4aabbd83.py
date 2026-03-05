import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
    """
    if isinstance(commands, str):
        commands = [commands]
    
    cmd = commands + args
    
    if verbose:
        print(f"Running command: {' '.join(cmd)}")
    
    process = subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT if hide_stderr else subprocess.PIPE,
        env=env,
        text=True
    )
    
    stdout, _ = process.communicate()
    
    if verbose:
        print(stdout)
    
    return {
        'stdout': stdout,
        'returncode': process.returncode
    }