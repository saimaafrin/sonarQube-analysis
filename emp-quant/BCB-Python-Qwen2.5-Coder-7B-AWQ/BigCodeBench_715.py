import sys
import subprocess
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'
def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    # Switch to the specified Python version
    subprocess.call([f'py{python_version}', '-m', 'pip', 'install', 'virtualenv'])
    subprocess.call([f'py{python_version}', '-m', 'virtualenv', 'myenv'])
    subprocess.call([f'py{python_version}', '-m', 'myenv', 'Scripts', 'activate'])
    
    # Add the specified path to sys.path
    sys.path.append(path_to_append)
    
    # Output the Python version that was switched to
    python_version = sys.version.split()[0]
    print(f"python_version: {python_version}")
    
    return python_version