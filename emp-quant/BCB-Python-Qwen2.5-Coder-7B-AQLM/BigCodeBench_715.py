
import sys
import subprocess
# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    # Get the current Python version
    current_version = sys.version.split()[0]
    
    # Construct the command to switch to the specified Python version
    command = f'python{python_version} -c "import sys; sys.path.append(\'{path_to_append}\'); print(sys.version.split()[0])"'
    
    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Check if the command was successful
    if result.returncode == 0:
        # Update the global Python version
        sys.version = result.stdout.strip()
        # Append the path to sys.path
        sys.path.append(path_to_append)
        # Return the new Python version
        return sys.version
    else:
        # Return the current Python version if the command failed
        return current_version