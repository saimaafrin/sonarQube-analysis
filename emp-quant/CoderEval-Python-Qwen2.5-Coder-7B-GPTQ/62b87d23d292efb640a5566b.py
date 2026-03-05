import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    cmd = commands + args
    
    if verbose:
        print(f"Running command: {' '.join(cmd)}")
    
    try:
        process = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
        
        if hide_stderr:
            _, stderr = process.communicate()
        else:
            stdout, stderr = process.communicate()
        
        if verbose and stderr:
            print(f"Stderr: {stderr.decode('utf-8')}")
        
        return process.returncode, stdout.decode('utf-8'), stderr.decode('utf-8')
    
    except Exception as e:
        if verbose:
            print(f"Error running command: {e}")
        return -1, None, str(e)