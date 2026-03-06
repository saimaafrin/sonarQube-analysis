
import subprocess
import os
import sys
import time

def task_func(script_path, wait=True, *args):
    """
    Run a Python script as a process with predefined arguments.

    Args:
        script_path (str): Path to the Python script to run.
        wait (bool, optional): Whether to wait for the process to complete. Defaults to True.
        *args: Additional arguments to pass to the script.

    Returns:
        int or None: The return code of the subprocess if 'wait' is True, otherwise None.

    Raises:
        ValueError: If the script does not exist.
        subprocess.CalledProcessError: If the script raises an exception.
    """
    # Check if the script exists
    if not os.path.isfile(script_path) or not script_path.endswith('.py'):
        raise ValueError(f"The script {script_path} does not exist.")

    # Construct the command to run the script
    command = [sys.executable, script_path] + list(args)

    try:
        if wait:
            # Wait for the process to complete and get the return code
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.returncode
        else:
            # Start the process without waiting
            subprocess.Popen(command)
            return None
    except subprocess.CalledProcessError as e:
        # Raise an exception if the script raises an error
        raise subprocess.CalledProcessError(e.returncode, e.cmd, e.output, e.stderr)