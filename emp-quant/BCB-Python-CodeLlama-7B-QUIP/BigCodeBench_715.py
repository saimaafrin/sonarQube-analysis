
import sys
import subprocess

# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    # Switch to the specified Python version
    subprocess.run(["python", "-m", "venv", "--clear", "--prompt", "venv", "--version", python_version])
    sys.path.append(path_to_append)
    print(f"Switched to Python {python_version} with {path_to_append} added to sys.path")