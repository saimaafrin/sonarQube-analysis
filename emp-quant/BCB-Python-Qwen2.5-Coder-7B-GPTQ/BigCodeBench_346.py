import subprocess
import os
import sys
import time
def task_func(script_path, wait=True, *args):
    """
    Run a Python script as a process with predefined arguments. By default, waits for the process to complete.
    If wait is False, the function returns None. Raises:
    - ValueError: If the script does not exist.
    - subprocess.CalledProcessError: If the script raises an exception.
    Returns:
    int: The return code of the subprocess. If 'wait' is False, returns None.
    """
    # Check if the script exists
    if not os.path.exists(script_path):
        raise ValueError(f"Script does not exist: {script_path}")

    # Prepare the command to run the script with arguments
    command = [sys.executable, script_path] + list(args)

    # Run the script as a subprocess
    try:
        if wait:
            # Wait for the process to complete and get the return code
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.returncode
        else:
            # Start the process and return None immediately
            subprocess.Popen(command)
            return None
    except subprocess.CalledProcessError as e:
        # Raise an exception if the script raises an exception
        raise subprocess.CalledProcessError(e.returncode, e.cmd, e.output, e.stderr)