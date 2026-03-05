import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    for cmd in commands:
        try:
            if verbose:
                print(f"Running command: {cmd} with args: {args}")
            
            process = subprocess.Popen([cmd] + args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT if hide_stderr else subprocess.PIPE, env=env)
            output, _ = process.communicate()
            
            if process.returncode != 0 and not hide_stderr:
                print(output.decode('utf-8'))
            
            if process.returncode != 0:
                raise Exception(f"Command '{cmd}' failed with return code {process.returncode}")
        
        except Exception as e:
            print(f"Error running command '{cmd}': {e}")
            return False
    
    return True