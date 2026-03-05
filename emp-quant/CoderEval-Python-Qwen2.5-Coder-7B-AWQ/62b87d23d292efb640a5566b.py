import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    for cmd in commands:
        try:
            result = subprocess.run([cmd] + args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
            if hide_stderr:
                result.stderr = b''
            if verbose:
                print(f"Command: {cmd} {' '.join(args)}")
                print(f"Output: {result.stdout.decode('utf-8')}")
                print(f"Error: {result.stderr.decode('utf-8')}")
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            if verbose:
                print(f"Error running command {cmd}: {e}")
            return 1, None, str(e).encode('utf-8')