import sys
import subprocess
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'
def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    # Check if the specified Python version is installed
    try:
        subprocess.check_output([f'python{python_version}', '--version'])
    except subprocess.CalledProcessError:
        raise ValueError(f"Python version {python_version} is not installed.")

    # Switch to the specified Python version
    sys.executable = f'python{python_version}'

    # Add the specified path to sys.path
    if path_to_append not in sys.path:
        sys.path.append(path_to_append)

    # Return the Python version that was switched to
    return sys.version.split()[0]