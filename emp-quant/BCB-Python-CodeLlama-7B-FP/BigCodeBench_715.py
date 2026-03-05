import sys
import subprocess
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'
def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    """
    Switch to a specific version of Python and add a specific path to sys.path.
    Note that: This function changes the global Python version and should be used carefully.
    """
    # Switch to the specified Python version
    subprocess.run(f'python{python_version} -m venv .venv', shell=True)
    subprocess.run(f'.venv/bin/python -m pip install --upgrade pip', shell=True)
    subprocess.run(f'.venv/bin/python -m pip install --upgrade setuptools', shell=True)
    subprocess.run(f'.venv/bin/python -m pip install --upgrade wheel', shell=True)

    # Add the specified path to sys.path
    sys.path.append(path_to_append)

    # Output the Python version that was switched to
    python_version = f'Python {python_version}'
    print(f'Switched to {python_version}')

    # Return the Python version that was switched to
    return python_version