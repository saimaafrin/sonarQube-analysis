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
        stderr = subprocess.STDOUT if verbose else subprocess.PIPE
    
    process = subprocess.Popen([commands[0]] + args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=stderr)
    
    if verbose:
        output, _ = process.communicate()
        print(output.decode())
    else:
        output, _ = process.communicate()
    
    return process.returncode, output.decode()