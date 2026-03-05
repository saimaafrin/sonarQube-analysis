
import sys
import subprocess
# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    # Switch to the specified Python version
    try:
        # Construct the command to switch Python version
        command = f'switch-python {python_version}'
        # Execute the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to switch Python version: {e}")
        return None

    # Add the specified path to sys.path
    try:
        # Append the path to sys.path
        sys.path.append(path_to_append)
    except Exception as e:
        print(f"Failed to add path to sys.path: {e}")
        return None

    # Return the Python version that was switched to
    return python_version