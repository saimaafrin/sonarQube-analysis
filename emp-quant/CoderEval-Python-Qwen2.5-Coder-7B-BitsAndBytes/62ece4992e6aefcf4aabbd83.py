import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
    """
    if isinstance(commands, str):
        commands = [commands]
    
    full_command = commands + args
    
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
    
    try:
        process = subprocess.Popen(
            full_command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT if hide_stderr else subprocess.PIPE,
            env=env
        )
        
        stdout, stderr = process.communicate()
        
        if verbose:
            print(f"Command output:\n{stdout.decode()}")
        
        return {
            'stdout': stdout.decode(),
            'returncode': process.returncode
        }
    
    except Exception as e:
        if verbose:
            print(f"Error running command: {e}")
        return {
            'stdout': '',
            'returncode': -1
        }