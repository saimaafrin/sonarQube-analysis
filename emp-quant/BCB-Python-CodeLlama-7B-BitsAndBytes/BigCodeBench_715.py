
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

    # Print the Python version and the updated sys.path
    print(f'Python version: {python_version}')
    print(f'sys.path: {sys.path}')

# Call the task function with the specified arguments
task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND)