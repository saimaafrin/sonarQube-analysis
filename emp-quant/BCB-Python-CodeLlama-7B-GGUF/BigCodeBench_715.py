
import sys
import subprocess

# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    # Switch to the specified Python version
    subprocess.run(['python', '-m', 'venv', '--python', python_version])

    # Add the specified path to sys.path
    sys.path.append(path_to_append)

    # Output the Python version that was switched to
    print(f'Switched to Python version: {python_version}')

# Call the function
task_func()