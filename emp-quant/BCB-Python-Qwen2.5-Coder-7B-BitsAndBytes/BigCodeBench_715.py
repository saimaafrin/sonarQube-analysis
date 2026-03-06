
import sys
import subprocess

# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    # Check if the specified Python version is installed
    try:
        subprocess.check_output([f'python{python_version}', '--version'])
    except subprocess.CalledProcessError:
        raise ValueError(f"Python version {python_version} is not installed.")

    # Switch to the specified Python version
    os.environ['PATH'] = f'/usr/bin/python{python_version}:{os.environ["PATH"]}'
    sys.executable = f'/usr/bin/python{python_version}'

    # Add the specified path to sys.path
    sys.path.append(path_to_append)

    # Output the current Python version
    print(f"Current Python version: {sys.version}")
    return sys.version