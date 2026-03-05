
import subprocess
import os
import sys
import time

def task_func(script_path, wait=True, *args):
    """
    Run a Python script as a process with predefined arguments.
    
    Parameters:
    script_path (str): The path to the Python script to run.
    wait (bool): Whether to wait for the process to complete. Defaults to True.
    *args: Arguments to pass to the script.
    
    Returns:
    int: The return code of the subprocess. If 'wait' is False, returns None.
    
    Raises:
    ValueError: If the script does not exist.
    subprocess.CalledProcessError: If the script raises an exception.
    """
    if not os.path.exists(script_path):
        raise ValueError(f"The script {script_path} does not exist.")
    
    try:
        if wait:
            result = subprocess.run([sys.executable, script_path] + list(args), check=True, capture_output=True, text=True)
            return result.returncode
        else:
            subprocess.Popen([sys.executable, script_path] + list(args))
            return None
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError(e.returncode, e.cmd, e.output, e.stderr)