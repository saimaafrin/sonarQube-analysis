
import sys
import subprocess
# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    # Save the current Python version
    current_version = sys.version.split()[0]

    # Switch to the specified Python version
    subprocess.run(['py', '-0', python_version, '-m', 'venv', 'temp_venv'], check=True)
    subprocess.run(['temp_venv/bin/activate'], check=True)

    # Add the specified path to sys.path
    sys.path.append(path_to_append)

    # Return the Python version that was switched to
    return python_version